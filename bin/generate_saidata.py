#!/usr/bin/env python3
import yaml
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

def generate_software_yaml(software_name, output_file="software.yaml"):
  # Define the base YAML structure
  base_yaml_standard = {
    "version": "0.1",
    "packages": {
      "default": {"name": software_name, "version": None, "install_options": None},
#      "dev": {"name": f"{software_name}-dev", "version": "latest", "install_options": None},
#      "doc": {"name": f"{software_name}-doc", "version": "latest", "install_options": None},
    },
    "services": {
      "default": {"name": software_name, "service_name": software_name}
    },
    "directories": {
      "config": {"path": f"/etc/{software_name}", "owner": "root", "group": "root", "mode": "0755"},
      "dotconf": {"path": f"/etc/{software_name}/conf.d", "owner": "root", "group": "root", "mode": "0755"},
      "log": {"path": f"/var/log/{software_name}", "owner": "root", "group": "root", "mode": "0755"},
      "data": None
    },
    "processes": {
      "default": {"path": software_name, "owner": "root", "group": "root"}
    },
    "ports": {
      "default": {"port": None, "protocol": "tcp"}
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
      "bitnami": {}
    },
    "charts": {
      "upstream": {},
      "bitnami": {}
    },
    "repos": {
      "upstream": {},
      "16": {},
      "18": {}
    },
    "urls": {
      "website": None,
      "issues": None,
      "documentation": None,
      "support": None,
      "source": None,
      "license": None,
      "changelog": None,
      "download": None,
      "icon": None
    },
    "language": None,
    "description": None,
    "category": {
      "default": None,
      "sub": None,
      "tags": None
    },
    "license": None,
    "platforms": [],
  }

  base_yaml = {
    "version": "0.1",
    "urls": {},
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
    }
  }

  # Initialize LLM
  llm = OpenAI(temperature=0)

  # Query for Settings
  settings_port = PromptTemplate(
    input_variables=["software"],
    template="Provide description (max 200 chars), default listening port, programming language, licence type (Open Source, Commercial or Public Domain), supported platfomrs (Linux, Windows MacOS), and category (default, subcategory, tags) for {software}. Reply with YAML as follows: \n" \
    "description: 'Description of the software' \n" \
    "ports:\n" \
    "  default:\n" \
    "    port: 80 \n" \
    "  ssl:\n" \
    "    port: 443 \n" \
    "language: 'Python' \n" \
    "license: 'Open Source' \n" \
    "platforms: ['Linux', 'MacOS'] \n" \
    "category: \n" \
    "  default: 'Web Server' \n" \
    "  sub: 'HTTP Server' \n" \
    "  tags: ['web', 'server', 'http'] \n" \
    "Use null for missing data."
  )
  settings_chain = LLMChain(llm=llm, prompt=settings_port)
  settings_data = yaml.safe_load(settings_chain.run(software=software_name))
  if settings_data:
    base_yaml.update({k: v for k, v in settings_data.items() if v is not None})

  # Query for URLs
  url_prompt = PromptTemplate(
    input_variables=["software"],
    template="Provide the relevant URLs for {software} as a YAML dictionary. Keys: website, issues, documentation, support, source, license, download, icon. Use null for missing."
  )
  url_chain = LLMChain(llm=llm, prompt=url_prompt)
  url_data = yaml.safe_load(url_chain.run(software=software_name))
  if url_data:
    base_yaml["urls"].update({k: v for k, v in url_data.items() if v is not None})

  # Query for container image
  container_prompt = PromptTemplate(
    input_variables=["software"],
    template="What is the official Docker image for {software}? Reply with YAML: image: 'image_name'"
  )
  container_chain = LLMChain(llm=llm, prompt=container_prompt)
  container_data = yaml.safe_load(container_chain.run(software=software_name))
  if container_data and "image" in container_data:
    base_yaml["containers"]["upstream"]["image"] = container_data["image"]

  # Query for actions/commands
#  actions_prompt = PromptTemplate(
#    input_variables=["software"],
#    template="List common CLI commands for {software} as YAML under 'actions: commands:'. Example for Apache includes test, info, version."
#  )
#  actions_chain = LLMChain(llm=llm, prompt=actions_prompt)
#  actions_data = yaml.safe_load(actions_chain.run(software=software_name))
#  if actions_data:
#    base_yaml["actions"] = actions_data.get("actions", actions_data)

  # Clean None/empty values
  def clean(data):
    if isinstance(data, dict):
      return {k: clean(v) for k, v in data.items() if v not in (None, [], {}, "") and clean(v) not in (None, [], {})}
    elif isinstance(data, list):
      return [clean(v) for v in data if v not in (None, [], {}, "") and clean(v) not in (None, [], {})]
    else:
      return data

  cleaned_yaml = clean(base_yaml)

  # Print the cleaned YAML to console
  print(yaml.dump(cleaned_yaml, sort_keys=False))
  # Write to YAML file
#  with open(output_file, 'w') as f:
#    yaml.dump(cleaned_yaml, f, sort_keys=False)
#    yaml.dump(base_yaml, f, sort_keys=False)
#  print(f"YAML file generated as {output_file}")

if __name__ == "__main__":
  import sys
  if len(sys.argv) < 2:
    print("Usage: python script.py <software_name>")
    sys.exit(1)
  software_name = sys.argv[1]
  generate_software_yaml(software_name)