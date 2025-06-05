#!/bin/bash
# First argument is the list file to use
if [ -z "$1" ]; then
  echo "Usage: $0 <list_file> [overwrite]"
  exit 1
fi
LIST_FILE="$1"
OVERWRITE="${2:-disable}"

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
  echo "Processing saidata for: $line"
  "${main_dir}/bin/generate_saidata.py" "$line" "$OVERWRITE" || {
    echo "Error: Failed to generate saidata for $line"
    continue
  }
  echo
done < "$LIST_FILE"