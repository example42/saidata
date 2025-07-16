#!/usr/bin/env python3
import yaml
import os
import json
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import re
import requests

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
    if not isinstance(llm_output, str):
        print(f"WARNING: llm_output is not a string, type: {type(llm_output)}")
        return ""
        
    # Remove markdown code block markers
    llm_output = re.sub(r'^```[a-zA-Z]*', '', llm_output, flags=re.MULTILINE)
    llm_output = llm_output.replace('```', '')
    # Remove leading/trailing whitespace and dots
    llm_output = llm_output.strip().lstrip('.')
    
    # Debug: Print the processed output
    print(f"DEBUG: Processed LLM output (first 200 chars): {llm_output[:200]}")
    
    # Remove any leading lines that are not YAML keys
    lines = llm_output.splitlines()
    for i, line in enumerate(lines):
        try:
            if line.strip().startswith('version:'):
                return '\n'.join(lines[i:])
        except Exception as e:
            print(f"ERROR: Exception processing line {i}: {line}")
            print(f"Exception: {e}")
            continue
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
  # Try to load base_yaml from saidata-0.1.schema.json if available
  schema_path = os.path.join(main_dir, "saidata-0.1.schema.json")
  if os.path.exists(schema_path):
    with open(schema_path, "r") as f:
      schema_json = json.load(f)
      # Try to extract the main schema properties
      if "properties" in schema_json:
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
        base_yaml = schema_props_to_yaml(schema_json["properties"])
        base_yaml["version"] = "0.1"
  else:
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
      "If {software} is not available for the provider, reply with:\nversion: 0.1\nsupported: false\n. "
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
  
  # Debug: Check if ai_message.content is a string
  if not hasattr(ai_message, 'content'):
    print(f"ERROR: ai_message does not have 'content' attribute. Type: {type(ai_message)}")
    print(f"ai_message: {ai_message}")
    raise ValueError("LLM response does not have expected 'content' attribute")
    
  all_info_raw = ai_message.content
  
  # Debug: Check if content is a string
  if not isinstance(all_info_raw, str):
    print(f"ERROR: ai_message.content is not a string. Type: {type(all_info_raw)}")
    print(f"Content: {all_info_raw}")
    raise ValueError("LLM response content is not a string")
    
  all_info_yaml = extract_yaml_from_llm_output(all_info_raw)
  
  # Debug: Print the extracted YAML
  print(f"DEBUG: Extracted YAML (first 200 chars): {all_info_yaml[:200]}")
  
  try:
    all_info_data = yaml.safe_load(all_info_yaml)
  except yaml.YAMLError as e:
    print(f"ERROR: Failed to parse YAML: {e}")
    print(f"YAML content: {all_info_yaml}")
    raise ValueError(f"Invalid YAML from LLM: {e}")
  except Exception as e:
    print(f"ERROR: Unexpected error parsing YAML: {e}")
    print(f"YAML content: {all_info_yaml}")
    raise
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

  # Clean the YAML first
  cleaned_yaml = clean(base_yaml)

  # --- Data validation checks ---

  # 1. URL checks: Ensure all URLs are valid if present
  def is_valid_url(url):
    if not url or not isinstance(url, str):
        return True  # Accept None or missing
    url_regex = re.compile(
        r'^(https?|ftp)://[^\s/$.?#].[^\s]*', re.IGNORECASE)
    if not url_regex.match(url):
        return False
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        return response.status_code < 400  # Return True if status code indicates success
    except requests.RequestException:
        return False  # Return False if request fails

  if "urls" in cleaned_yaml and isinstance(cleaned_yaml["urls"], dict):
      for url_key, url_val in cleaned_yaml["urls"].items():
          if url_val and not is_valid_url(url_val):
              print(f"WARNING: {url_key} URL '{url_val}' is not a valid URL.")

  # 2. Ports check: Ensure ports are integers or None
  if "ports" in cleaned_yaml and isinstance(cleaned_yaml["ports"], dict):
      for port_key, port_val in cleaned_yaml["ports"].items():
          if port_val is not None and not isinstance(port_val, int):
              try:
                  cleaned_yaml["ports"][port_key] = int(port_val)
              except Exception:
                  print(f"WARNING: Port '{port_key}' value '{port_val}' is not an integer or convertible.")

  # 3. Platforms check: Ensure platforms are among allowed values
  allowed_platforms = {"linux", "windows", "macos"}
  if "platforms" in cleaned_yaml and isinstance(cleaned_yaml["platforms"], list):
      cleaned_yaml["platforms"] = [
          p.lower() for p in cleaned_yaml["platforms"] if isinstance(p, str) and p.lower() in allowed_platforms
      ]

  # 4. License check: Accept only Open Source, Commercial, or Public Domain (case-insensitive)
  allowed_licenses = {"open source", "commercial", "public domain"}
  if "license" in cleaned_yaml and cleaned_yaml["license"]:
      lic = str(cleaned_yaml["license"]).strip().lower()
      if lic not in allowed_licenses:
          print(f"WARNING: License '{cleaned_yaml['license']}' is not one of {allowed_licenses}.")

  # 5. Category check: Ensure keys exist and are strings or None
  if "category" in cleaned_yaml and isinstance(cleaned_yaml["category"], dict):
      for cat_key in ["default", "sub", "tags"]:
          if cat_key not in cleaned_yaml["category"]:
              cleaned_yaml["category"][cat_key] = None

  # 6. Docker image check: Ensure containers.upstream.image is a non-empty string
  try:
      image_val = cleaned_yaml["containers"]["upstream"]["image"]
      if not image_val or not isinstance(image_val, str):
          print("WARNING: Docker image is missing or not a string.")
  except Exception:
      print("WARNING: containers.upstream.image is missing.")

  # Additional checks (optional): MCP provider/package checks would require integration with provider logic

  # --- AI feedback and integration step ---

  # Gather results of checks
  checks_summary = []
  # 1. URL checks
  if "urls" in cleaned_yaml and isinstance(cleaned_yaml["urls"], dict):
      for url_key, url_val in cleaned_yaml["urls"].items():
          if url_val and not is_valid_url(url_val):
              checks_summary.append(f"WARNING: {url_key} URL '{url_val}' is not a valid URL.")
  # 2. Ports check
  if "ports" in cleaned_yaml and isinstance(cleaned_yaml["ports"], dict):
      for port_key, port_val in cleaned_yaml["ports"].items():
          if port_val is not None and not isinstance(port_val, int):
              try:
                  int(port_val)
              except Exception:
                  checks_summary.append(f"WARNING: Port '{port_key}' value '{port_val}' is not an integer or convertible.")
  # 3. Platforms check
  if "platforms" in cleaned_yaml and isinstance(cleaned_yaml["platforms"], list):
      for p in cleaned_yaml["platforms"]:
          if p not in allowed_platforms:
              checks_summary.append(f"WARNING: Platform '{p}' is not in allowed list {allowed_platforms}.")
  # 4. License check
  if "license" in cleaned_yaml and cleaned_yaml["license"]:
      lic = str(cleaned_yaml["license"]).strip().lower()
      if lic not in allowed_licenses:
          checks_summary.append(f"WARNING: License '{cleaned_yaml['license']}' is not one of {allowed_licenses}.")
  # 5. Docker image check
  try:
      image_val = cleaned_yaml["containers"]["upstream"]["image"]
      if not image_val or not isinstance(image_val, str):
          checks_summary.append("WARNING: Docker image is missing or not a string.")
  except Exception:
      checks_summary.append("WARNING: containers.upstream.image is missing.")

  # Compose feedback prompt for AI
  feedback_prompt = PromptTemplate(
      input_variables=["software", "checks", "current_yaml"],
      template=(
          "You previously generated the following YAML for {software}:\n"
          "{current_yaml}\n"
          "The following issues or warnings were found during validation:\n"
          "{checks}\n"
          "Please review these issues and suggest corrections or improvements. "
          "Return the corrected YAML in the same structure. If you agree with the current YAML, return it unchanged."
      )
  )
  checks_str = "\n".join(checks_summary) if checks_summary else "No issues found."
  current_yaml_str = yaml.dump(cleaned_yaml, sort_keys=False)
  ai_feedback_message = (feedback_prompt | llm).invoke({
      "software": software_name,
      "checks": checks_str,
      "current_yaml": current_yaml_str
  })
  ai_feedback_yaml = extract_yaml_from_llm_output(ai_feedback_message.content)
  try:
      ai_feedback_data = yaml.safe_load(ai_feedback_yaml)
      if ai_feedback_data:
          cleaned_yaml = clean(ai_feedback_data)
  except Exception:
      # If parsing fails, keep previous cleaned_yaml
      pass

  # --- Conversation and output logging ---
  conversation_log = []
  conversation_log.append("=== Initial Prompt to AI ===\n" + all_info_prompt.format(software=software_name, base_yaml=base_yaml_str))
  conversation_log.append("=== AI Initial Output ===\n" + all_info_raw)
  conversation_log.append("=== Validation Checks ===\n" + checks_str)
  conversation_log.append("=== Feedback Prompt to AI ===\n" + feedback_prompt.format(software=software_name, checks=checks_str, current_yaml=current_yaml_str))
  conversation_log.append("=== AI Feedback Output ===\n" + ai_feedback_message.content)
  conversation_log.append("=== Final YAML ===\n" + yaml.dump(cleaned_yaml, sort_keys=False))

  os.makedirs(software_dir, exist_ok=True)

  # Write conversation log to file
  log_file = os.path.join(software_dir, "generation_conversation.log")
  with open(log_file, "w") as f:
      f.write("\n\n".join(conversation_log))

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
#        cleaned_provider_yaml = {"version": "0.1", "supported": ToCheck}
        cleaned_provider_yaml = clean(provider_data)
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
      'apt', 'yum', 'zypper', 'dnf', 'snap', 'flatpak', 'scoop', 'choco', 'brew', 'winget', 'nix', 'pip', 'pipx', 'conda', 'docker', 'helm', 'maven', 'gradle', 'npm', 'yarn', 'composer', 'nuget', 'gem', 'cargo', 'go get', 'crates.io', 'leiningen', 'cabal', 'stack', 'cpan','pacman', 'apk', 'portage', 'xbps', 'slackpkg', 'opkg', 'emerge', 'guix', 'fink', 'macports', 'spack', 'pkg', 'nixpkgs'
    ]
    generate_all_providers_yaml(software_name, provider_list, overwrite=overwrite_method, model=openai_model)
