#!/bin/bash
# First argument is the list file to use
if [ -z "$1" ]; then
  echo "Usage: $0 <list_file>"
  exit 1
fi
LIST_FILE="$1"

# set main_dir to git root directory
main_dir=$(git rev-parse --show-toplevel)

# Check if the list file exists 
if [ ! -f "$LIST_FILE" ]; then
  echo "List file '$LIST_FILE' does not exist."
  exit 1
fi
# Read the list file and generate the mass files
while IFS= read -r line; do
  # Skip empty lines and comments
  if [[ -z "$line" || "$line" =~ ^# ]]; then
    continue
  fi
  # Generate saidata under software/$software_name_2_initials/$software_name/defaults.yaml
  software_name=$(echo "$line" | cut -d'/' -f1)
  software_name_2_initials=$(echo "$software_name" | awk '{print substr($0, 1, 2)}')
  # Check if saidata has already been generated
  if [ -f "${main_dir}/software/${software_name_2_initials}/${software_name}/defaults.yaml" ]; then
    echo "Saidata for $software_name already exists, skipping."
    continue
  fi
  echo "Processing saidata for: $software_name"
  # Create the directory structure if it doesn't exist
  mkdir -p "${main_dir}/software/${software_name_2_initials}/${software_name}"
  # Call the Python script to generate the mass file
  "${main_dir}/bin/generate_saidata.py" "$software_name" 2> /dev/null > "${main_dir}/software/${software_name_2_initials}/${software_name}/defaults.yaml"
  if [ $? -ne 0 ]; then
    echo "Failed to generate saidata for $software_name"
    continue
  fi
  echo
done < "$LIST_FILE"