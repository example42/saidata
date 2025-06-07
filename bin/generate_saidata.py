#!/usr/bin/env python3
import yaml
import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

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
def generate_default_yaml(software_name, overwrite="disable"):

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
      "sbom": None,
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
  llm = OpenAI(temperature=0)

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
  all_info_raw = (all_info_prompt | llm).invoke({"software": software_name, "base_yaml": base_yaml_str})
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
def generate_provider_yaml(software_name, provider_name, overwrite="disable"):
  provider_dir = os.path.join(software_dir, "providers")
  output_file = os.path.join(provider_dir, f"{provider_name}.yaml")

  if overwrite == "disable" and os.path.exists(output_file):
    print(f"File {output_file} already exists. Skipping generation.")
    return

  # Base YAML structure for provider
  base_provider_yaml = {
    "version": "0.1",
    "directories": {
      "config": {"path": None},
      "dotconf": {"path": None},
      "log": {"path": None},
      "data": {"path": None},
      "lib": {"path": None}
    },
    "files": {
      "config": {"path": None},
      "log": {"path": None},
      "pid": {"path": None}
    },
    "packages": {
      "default": {"name": None}
    },
    "services": {
      "default": {"name": None}
    },
    "processes": {
      "default": {"path": None}
    }
  }

  # Initialize LLM
  llm = OpenAI(temperature=0)

  # Convert base_provider_yaml to YAML string for prompt
  base_provider_yaml_str = yaml.dump(base_provider_yaml, sort_keys=False)

  # Query for provider-specific settings
  settings_prompt = PromptTemplate(
    input_variables=["software", "provider", "base_yaml"],
    template=(
      "Check official {software} and {provider} sites to verify if {provider} can install {software}. If it can't reply with:\nversion: 0.1\nsupported: false\n."      
      "Otherwise Provide the configuration settings for {software} installation and management using {provider}. "
      "Provide only data for sure you have correct answers, use null for missing data. Output as YAML with the following structure:\n{base_yaml}"

    )
  )
  settings_raw = (settings_prompt | llm).invoke({"software": software_name, "provider": provider_name, "base_yaml": base_provider_yaml_str})
  settings_yaml = extract_yaml_from_llm_output(settings_raw)
  settings_data = yaml.safe_load(settings_yaml)
  
  if settings_data:
    if settings_data.get("supported") is False:
      base_provider_yaml = {"version": "0.1", "supported": False}
    else:
      base_provider_yaml.update({k: v for k, v in settings_data.items() if v is not None})

  # Clean None/empty values
  cleaned_provider_yaml = clean(base_provider_yaml)

  os.makedirs(provider_dir, exist_ok=True)

  # Write to YAML file if overwrite is enabled or if the file does not exist
  if overwrite == "enable" or not os.path.exists(output_file):
    with open(output_file, 'w') as f:
      yaml.dump(cleaned_provider_yaml, f, sort_keys=False)
  elif overwrite == "merge":
    # If merge, read existing file and update it
    if os.path.exists(output_file):
      with open(output_file, 'r') as f:
        existing_yaml = yaml.safe_load(f) or {}
      existing_yaml.update(cleaned_provider_yaml)
      cleaned_provider_yaml = existing_yaml
      with open(output_file, 'w') as f:
        yaml.dump(cleaned_provider_yaml, f, sort_keys=False)
  else:
    print(f"Skipping write to {output_file} as overwrite is disabled.")


if __name__ == "__main__":
  import sys
  if len(sys.argv) < 2:
    print("Usage: python script.py <software_name> [overwrite_method]")
    sys.exit(1)
  software_name = sys.argv[1]
  overwrite_method = sys.argv[2] if len(sys.argv) > 2 else "disable"

  software_initials = software_name[:2].lower()
  software_dir = os.path.join(main_dir, "software", software_initials, software_name)
  output_file = os.path.join(software_dir, "defaults.yaml")

  if overwrite_method not in ["disable", "enable", "merge"]:
    raise ValueError("Invalid overwrite method. Use 'disable', 'enable', or 'merge'.")
  generate_default_yaml(software_name, overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'apt', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'yum', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'zypper', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'dnf', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'snap', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'flatpak', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'scoop', overwrite=overwrite_method) 
  generate_provider_yaml(software_name, 'chocolatey', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'brew', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'winget', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'nix', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'gem', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'pip', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'nuget', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'npm', overwrite=overwrite_method)
  generate_provider_yaml(software_name, 'nix', overwrite=overwrite_method)
#  generate_provider_yaml(software_name, 'maven', overwrite=overwrite_method)
