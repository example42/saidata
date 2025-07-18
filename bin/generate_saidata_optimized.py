#!/usr/bin/env python3
import yaml
import os
import json
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

main_dir = None
main_dir = os.popen("git rev-parse --show-toplevel").read().strip()

# If main_dir is not set throw and error and exit
if not main_dir:
  raise ValueError("Please run this script from saidata git repo directory.")

### Clean function to remove None or empty values from YAML ###
def clean(data):
  if isinstance(data, dict):
    return {k: clean(v) for k, v in data.items() if v not in (None, [], {}, "") and clean(v) not in (None, [], {})}
  elif isinstance(data, list):
    return [clean(v) for v in data if v not in (None, [], {}, "") and clean(v) not in (None, [], {})]
  else:
    return data

def extract_yaml_from_llm_output(llm_output):
    """
    Extracts the YAML part from LLM output, removing markdown/code block markers and leading/trailing text.
    """
    import re
    # Remove markdown code block markers
    llm_output = re.sub(r'^```[a-zA-Z]*', '', llm_output, flags=re.MULTILINE)
    llm_output = llm_output.replace('```', '')
    # Remove leading/trailing whitespace and dots
    llm_output = llm_output.strip().lstrip('.')
    # Remove any leading lines that are not YAML keys
    lines = llm_output.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('version:'):
            return '\n'.join(lines[i:])
    return llm_output

### MAIN FUNCTION TO GENERATE DEFAULT YAML FILES ###
def generate_default_yaml(software_name, overwrite="disable", model=None):

  # If overwrite is disable and file exists, do not overwrite and exit
  if overwrite not in ["disable", "enable", "merge"]:
    raise ValueError("Invalid overwrite method. Use 'disable', 'enable', or 'merge'.")

  if overwrite == "disable":
    if os.path.exists(output_file):
      print(f"File {output_file} already exists. Skipping generation.")
      return
  # Base YAML structure
  base_yaml = {
    "version": "0.1",
    "description": None,
    "language": None,
    "ports": { # If not applicable do not include this key
      "default": None,  # Default port
      "ssl": None       # SSL port
    },
    "category": {
      "default": None,  # Default is undefined.
      "sub": None,      # Default is undefined.
      "tags": None      # Default is undefined.
    },
    "license": None,  # Default is undefined.
    "platforms": [],  # Array of supported platforms, e.g. [linux, windows, macos]
    "urls": {
      "website": None,
      "issues": None,
      "documentation": None,
      "support": None,
      "source": None,
      "license": None,
      "download": None,
      "icon": None
    },
    "containers": {
      "upstream": {
        "name": software_name,
        "image": software_name,
        "version": "latest",
        "network": None,
        "ports": [],
        "volumes": [],
        "nodaemon_args": None,
        "env": []
      },
    },

  }

  # Initialize LLM
  llm = ChatOpenAI(model=model, temperature=0)

  # Convert base_yaml to YAML string for prompt
  base_yaml_str = yaml.dump(base_yaml, sort_keys=False)

  # Single optimized prompt for all metadata, using base_yaml
  all_info_prompt = PromptTemplate(
    input_variables=["software", "base_yaml"],
    template=(
      "If {software} is not available for any platform, reply with:\nversion: 0.1\nsupported: false\n. "
      "Otherwise, provide the following information for {software} as a YAML dictionary, using the following structure as a base:\n{base_yaml}\n"
      "Fill in: description (max 200 chars), ports (if applicable), language, license (Open Source, Commercial or Public Domain), "
      "platforms (specify only the supported ones among Linux, Windows, MacOS), category (default, sub, tags), URLs (website, issues, documentation, support, source, license, download, icon), "
      "and the official Docker image (image). Do not include key for missing data, use null for missing values. "
    )
  )
  # Invoke LLM and pull out the content string
  ai_message = (all_info_prompt | llm).invoke({
    "software": software_name,
    "base_yaml": base_yaml_str
  })
  all_info_raw = ai_message.content
  all_info_yaml = extract_yaml_from_llm_output(all_info_raw)
  all_info_data = yaml.safe_load(all_info_yaml)
  if all_info_data:
    if all_info_data.get("supported") is False:
      base_yaml = {"version": "0.1", "supported": False}
    else:
      for k, v in all_info_data.items():
        if k == "urls" and v:
          base_yaml["urls"].update({uk: uv for uk, uv in v.items() if uv is not None})
        elif k == "containers" and v:
          base_yaml["containers"].update(v)
        elif k == "image" and v:
          base_yaml["containers"]["upstream"]["image"] = v
        elif v is not None:
          base_yaml[k] = v

  cleaned_yaml = clean(base_yaml)

  os.makedirs(software_dir, exist_ok=True)

  # Write to YAML file if overwrite is enabled or if the file does not exist
  if overwrite == "enable" or not os.path.exists(output_file):
    with open(output_file, 'w') as f:
      yaml.dump(cleaned_yaml, f, sort_keys=False)
  elif overwrite == "merge":
    # If merge, read existing file and update it
    if os.path.exists(output_file):
      with open(output_file, 'r') as f:
        existing_yaml = yaml.safe_load(f) or {}
      existing_yaml.update(cleaned_yaml)
      cleaned_yaml = existing_yaml
      with open(output_file, 'w') as f:
        yaml.dump(cleaned_yaml, f, sort_keys=False)
  else:
    print(f"Skipping write to {output_file} as overwrite is disabled.")

### FUCTION TO GENERATE PROVIDER YAML FILES ###
def generate_all_providers_yaml(software_name, provider_names, overwrite="disable", model=None):
  provider_dir = os.path.join(software_dir, "providers")
  os.makedirs(provider_dir, exist_ok=True)

  # Base YAML structure for provider is baes on the json schema in saidata-0.1.schema.json
  # 
  base_provider_yaml = {
    "version": "0.1",
    "supported": None,
    "description": None,
    "install": {
      "package": None,
      "version": None,
      "repo": None,
      "options": None
    },
    "uninstall": {
      "package": None,
      "options": None
    },
    "update": {
      "package": None,
      "options": None
    },
    "notes": None
  }
  # Load base_provider_yaml from saidata-0.1.schema.json if available
  schema_path = os.path.join(main_dir, "saidata-0.1.schema.json")
  if os.path.exists(schema_path):
    with open(schema_path, "r") as f:
      schema_json = json.load(f)
      # Try to extract the provider schema if present
      if "definitions" in schema_json and "provider" in schema_json["definitions"]:
        provider_props = schema_json["definitions"]["provider"].get("properties", {})
        # Convert JSON schema properties to a YAML-like dict with None as default values
        def schema_props_to_yaml(props):
          result = {}
          for k, v in props.items():
            if v.get("type") == "object" and "properties" in v:
              result[k] = schema_props_to_yaml(v["properties"])
            elif v.get("type") == "array":
              result[k] = []
            else:
              result[k] = None
          return result
        base_provider_yaml = schema_props_to_yaml(provider_props)
        base_provider_yaml["version"] = "0.1"
  llm = ChatOpenAI(model=model, temperature=0)
  base_provider_yaml_str = yaml.dump(base_provider_yaml, sort_keys=False)

  # Single prompt for all providers
  all_providers_prompt = PromptTemplate(
    input_variables=["software", "providers", "base_yaml"],
    template=(
      "Generate a yaml based on {base_yaml} specs for each provider of this lisr {providers} for the software: {software}."
      "Be sure to check if a given provider can install or manage the software. If it can't, return an empty YAML structure with version 0.1 and supported: false. "
      "If it can, provide the configuration settings for installation and management using that provider. "
      "File output should be a valid YAML dictionary where each key is a provider name and the value is the data for that provider in format {base_yaml}. "
    )
  )
  providers_str = ", ".join(provider_names)
  ai_message = (all_providers_prompt | llm).invoke({
        "software": software_name,
        "providers": providers_str,
        "base_yaml": base_provider_yaml_str
      })
  all_providers_raw = ai_message.content
  # Write the raw output to a file for debugging
  with open(os.path.join(provider_dir, "all_providers_raw.txt"), 'w') as f:
    f.write(all_providers_raw)
  all_providers_yaml = extract_yaml_from_llm_output(all_providers_raw)
  all_providers_data, valid_lines = safe_partial_yaml_load(all_providers_yaml)
  if all_providers_data is None:
      print("ERROR: Could not parse any valid YAML from LLM output!")
      print("Raw YAML output was:")
      print(all_providers_yaml)
      raise RuntimeError("No valid YAML could be parsed.")
  if valid_lines < len(all_providers_yaml.strip().splitlines()):
      print("WARNING: LLM output was incomplete YAML. Parsed only the valid part at the top.")

  for provider in provider_names:
    output_file = os.path.join(provider_dir, f"{provider}.yaml")
    provider_data = all_providers_data.get(provider, None)
    if provider_data:
      if provider_data.get("supported") is False:
        cleaned_provider_yaml = {"version": "0.1", "supported": False}
      else:
        cleaned_provider_yaml = clean(provider_data)
    else:
      cleaned_provider_yaml = {"version": "0.1", "supported": False}

    if overwrite == "enable" or not os.path.exists(output_file):
      with open(output_file, 'w') as f:
        yaml.dump(cleaned_provider_yaml, f, sort_keys=False)
    elif overwrite == "merge":
      if os.path.exists(output_file):
        with open(output_file, 'r') as f:
          existing_yaml = yaml.safe_load(f) or {}
        existing_yaml.update(cleaned_provider_yaml)
        cleaned_provider_yaml = existing_yaml
        with open(output_file, 'w') as f:
          yaml.dump(cleaned_provider_yaml, f, sort_keys=False)
    else:
      print(f"Skipping write to {output_file} as overwrite is disabled.")

def safe_partial_yaml_load(yaml_text):
    """
    Try to load as much valid YAML as possible from the top of the string.
    If parsing fails, iteratively remove lines from the end until it succeeds or nothing is left.
    """
    lines = yaml_text.strip().splitlines()
    while lines:
        try:
            return yaml.safe_load('\n'.join(lines)), len(lines)
        except yaml.YAMLError:
            lines = lines[:-1]
    return None, 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <software_name> [overwrite_method] [openai_model]")
        sys.exit(1)
    software_name = sys.argv[1]
    overwrite_method = sys.argv[2] if len(sys.argv) > 2 else "disable"
    openai_model = sys.argv[3] if len(sys.argv) > 3 else "gpt-4.1"  # Default model

    software_initials = software_name[:2].lower()
    software_dir = os.path.join(main_dir, "software", software_initials, software_name)
    output_file = os.path.join(software_dir, "defaults.yaml")

    if overwrite_method not in ["disable", "enable", "merge"]:
      raise ValueError("Invalid overwrite method. Use 'disable', 'enable', or 'merge'.")
    generate_default_yaml(software_name, overwrite=overwrite_method, model=openai_model)
    provider_list = [
      'apt', 'yum', 'zypper', 'dnf', 'snap', 'flatpak', 'scoop', 'chocolatey', 'brew', 'winget', 'nix', 'pip', 'pipx', 'conda', 'docker', 'helm', 'maven', 'gradle', 'npm', 'yarn', 'composer', 'nuget', 'gem', 'cargo', 'go get', 'crates.io', 'leiningen', 'cabal', 'stack', 'cpan'
    ]
    generate_all_providers_yaml(software_name, provider_list, overwrite=overwrite_method, model=openai_model)
