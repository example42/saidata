#!/bin/bash
#
# Comprehensive Metadata Fetching Script for AI Datasets
#
# This script downloads package metadata from a wide variety of package manager
# repositories. The collected data is intended for use in building datasets
# for Retrieval-Augmented Generation (RAG) or for fine-tuning language models.
#
# The script now fetches data for multiple OS/distro versions where applicable
# and saves all metadata into a structured directory tree under ./metadata_dump/.
#

set -e

# --- Configuration ---
OUTPUT_DIR="metadata_dump"
echo "Starting metadata fetch process. Output will be saved to: ${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

# --- Helper Functions ---

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# --- Prerequisite Check ---
echo "Checking for required tools..."
for tool in git curl jq; do
    if ! command_exists ${tool}; then
        echo "Error: Required tool '${tool}' is not installed. Please install it to continue."
        exit 1
    fi
done
echo "All required tools are present."
echo "----------------------------------------"


# --- Fetch Functions ---

fetch_apt() {
    local name="apt"
    echo "Fetching metadata for ${name}..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    
    # Define different distro versions to fetch
    local targets=(
        "debian,bullseye,https://deb.debian.org/debian/dists/bullseye"
        "debian,bookworm,https://deb.debian.org/debian/dists/bookworm"
        "ubuntu,focal,http://archive.ubuntu.com/ubuntu/dists/focal"
        "ubuntu,jammy,http://archive.ubuntu.com/ubuntu/dists/jammy"
    )

    for target in "${targets[@]}"; do
        IFS=',' read -r distro version url <<< "$target"
        echo "  - Fetching ${distro} ${version} (main, amd64)..."
        # Fetching for main component, amd64 architecture
        curl -s "${url}/main/binary-amd64/Packages.gz" -o "${dir}/${distro}_${version}_main_amd64_Packages.gz"
        gunzip -f "${dir}/${distro}_${version}_main_amd64_Packages.gz"
    done
    echo "SUCCESS: Saved Debian/Ubuntu 'Packages' files to ${dir}/"
}

fetch_dnf() {
    local name="dnf"
    echo "Fetching metadata for ${name}..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"

    local targets=(
        "fedora,38,http://dl.fedoraproject.org/pub/fedora/linux/releases/38/Everything/x86_64/os/"
        "fedora,39,http://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os/"
        "centos,stream9,http://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/"
    )

    for target in "${targets[@]}"; do
        IFS=',' read -r distro version repo_url <<< "$target"
        echo "  - Fetching ${distro} ${version}..."
        local repomd_path="${dir}/${distro}_${version}_repomd.xml"
        curl -s "${repo_url}repodata/repomd.xml" -o "${repomd_path}"
        
        # Use grep with -oP for Perl-compatible regex to extract the href
        local primary_path=$(grep -oP '(?<=location href=")[^"]*primary.xml.gz' "${repomd_path}" || true)
        
        if [ -n "$primary_path" ]; then
            curl -s "${repo_url}${primary_path}" -o "${dir}/${distro}_${version}_primary.xml.gz"
            gunzip -f "${dir}/${distro}_${version}_primary.xml.gz"
        else
            echo "    - WARNING: Could not find primary.xml.gz path for ${distro} ${version}. Skipping."
        fi
    done
    echo "SUCCESS: Saved Fedora/CentOS 'repomd.xml' and 'primary.xml' files to ${dir}/"
}

fetch_winget() {
    local name="winget"
    echo "Fetching metadata for ${name} (Git clone)..."
    local dir="${OUTPUT_DIR}/${name}"
    if [ -d "${dir}" ]; then
        echo "  - Directory exists. Pulling latest changes."
        (cd "${dir}" && git pull)
    else
        git clone --depth 1 https://github.com/microsoft/winget-pkgs.git "${dir}"
    fi
    echo "SUCCESS: Cloned winget-pkgs repository to ${dir}/. Manifests are organized by version inside."
}

fetch_brew() {
    local name="brew"
    echo "Fetching metadata for ${name} (JSON API)..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    # The Homebrew API provides a single master file containing all formulae/casks and their versions.
    # This is the most efficient way to get the complete dataset.
    echo "  - Fetching all formulae..."
    curl -s "https://formulae.brew.sh/api/formula.json" | jq . > "${dir}/formulae_all.json"
    echo "  - Fetching all casks..."
    curl -s "https://formulae.brew.sh/api/cask.json" | jq . > "${dir}/casks_all.json"
    echo "SUCCESS: Saved Homebrew formulae and casks JSON to ${dir}/"
}

fetch_nix() {
    local name="nix"
    echo "Fetching metadata for ${name} (Git clone)..."
    local dir="${OUTPUT_DIR}/${name}"
    if [ -d "${dir}" ]; then
        echo "  - Directory exists. Pulling latest changes."
        (cd "${dir}" && git pull)
    else
        git clone --depth 1 https://github.com/NixOS/nixpkgs.git "${dir}"
    fi
    echo "SUCCESS: Cloned nixpkgs repository to ${dir}/. Nix expressions inherently handle versions."
}

fetch_npm() {
    local name="npm"
    echo "Fetching metadata for ${name} (API)..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    local packages=("react" "express" "lodash")
    echo "  - Fetching example packages and splitting by version..."
    for pkg in "${packages[@]}"; do
        local pkg_dir="${dir}/${pkg}"
        mkdir -p "${pkg_dir}"
        echo "    - Fetching full metadata for ${pkg}..."
        local full_json
        full_json=$(curl -s "https://registry.npmjs.org/${pkg}")
        
        # Save each version's metadata to a separate file
        echo "$full_json" | jq -r '.versions | keys[]' | while read -r version; do
            echo "$full_json" | jq --arg v "$version" '.versions[$v]' > "${pkg_dir}/${version}.json"
        done
    done
    echo "SUCCESS: Saved example npm package versions to ${dir}/"
}

fetch_pypi() {
    local name="pip"
    echo "Fetching metadata for ${name} (API)..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    local packages=("requests" "pandas" "numpy")
    echo "  - Fetching example packages and splitting by version..."
    for pkg in "${packages[@]}"; do
        local pkg_dir="${dir}/${pkg}"
        mkdir -p "${pkg_dir}"
        echo "    - Fetching full metadata for ${pkg}..."
        local full_json
        full_json=$(curl -s "https://pypi.org/pypi/${pkg}/json")

        # Save each release's metadata to a separate file
        echo "$full_json" | jq -r '.releases | keys[]' | while read -r version; do
             # The release value is an array, we take the first element if it exists
            echo "$full_json" | jq --arg v "$version" '.releases[$v] | .[0]' > "${pkg_dir}/${version}.json"
        done
    done
    echo "SUCCESS: Saved example PyPI package versions to ${dir}/"
}

fetch_cargo() {
    local name="cargo"
    echo "Fetching metadata for ${name} (Git index)..."
    local dir="${OUTPUT_DIR}/${name}"
    local index_dir="${dir}/crates.io-index"
    if [ -d "${index_dir}" ]; then
        echo "  - Directory exists. Pulling latest changes."
        (cd "${index_dir}" && git pull)
    else
        git clone --depth 1 https://github.com/rust-lang/crates.io-index.git "${index_dir}"
    fi
    echo "SUCCESS: Cloned crates.io-index repository to ${index_dir}/. The index contains versioned, line-delimited JSON."
}

fetch_helm() {
    local name="helm"
    echo "Fetching metadata for ${name}..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    local repos=(
        "bitnami,https://charts.bitnami.com/bitnami/index.yaml"
        "helm-stable,https://charts.helm.sh/stable/index.yaml"
    )
    for repo in "${repos[@]}"; do
        IFS=',' read -r repo_name repo_url <<< "$repo"
        echo "  - Fetching index for ${repo_name}..."
        curl -s "${repo_url}" -o "${dir}/${repo_name}_index.yaml"
    done
    echo "SUCCESS: Saved Helm chart indices to ${dir}/"
}

fetch_go() {
    local name="go"
    echo "Fetching metadata for ${name}..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    # The Go checksum database provides a continually updated log of all known modules and versions.
    echo "  - Fetching latest Go checksum database snapshot..."
    curl -s "https://sum.golang.org/latest" -o "${dir}/go_sum_db_latest.txt"
    echo "SUCCESS: Saved latest Go checksum database entries to ${dir}/"
}

fetch_flatpak() {
    local name="flatpak"
    echo "Fetching metadata for ${name} (Flathub Git)..."
    local dir="${OUTPUT_DIR}/${name}"
    if [ -d "${dir}" ]; then
        echo "  - Directory exists. Pulling latest changes."
        (cd "${dir}" && git pull)
    else
        # This is a large repo of all manifests, clone it with depth 1.
        git clone --depth 1 https://github.com/flathub/flathub.git "${dir}"
    fi
    echo "SUCCESS: Cloned Flathub manifest repository to ${dir}/"
}

fetch_scoop() {
    local name="scoop"
    echo "Fetching metadata for ${name} (Git buckets)..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    local buckets=(
        "main,https://github.com/ScoopInstaller/Main.git"
        "extras,https://github.com/ScoopInstaller/Extras.git"
    )
    for bucket in "${buckets[@]}"; do
        IFS=',' read -r bucket_name bucket_url <<< "$bucket"
        local bucket_dir="${dir}/${bucket_name}"
        echo "  - Fetching bucket '${bucket_name}'..."
        if [ -d "${bucket_dir}" ]; then
            (cd "${bucket_dir}" && git pull)
        else
            git clone --depth 1 "${bucket_url}" "${bucket_dir}"
        fi
    done
    echo "SUCCESS: Cloned Scoop buckets to ${dir}/"
}

fetch_hackage() {
    local name="hackage"
    echo "Fetching metadata for ${name} (Cabal)..."
    local dir="${OUTPUT_DIR}/${name}"
    mkdir -p "${dir}"
    # The Hackage index contains all .cabal files with all version information.
    echo "  - Fetching Hackage index tarball..."
    curl -s "https://hackage.haskell.org/01-index.tar.gz" -o "${dir}/01-index.tar.gz"
    (cd "${dir}" && tar -xzf "01-index.tar.gz" && rm "01-index.tar.gz")
    echo "SUCCESS: Extracted Hackage index to ${dir}/"
}

# --- Main Execution Logic ---

echo "Starting metadata fetch for all configured repositories."
echo "========================================================"

fetch_apt
echo "----------------------------------------"
fetch_dnf
echo "----------------------------------------"
fetch_winget
echo "----------------------------------------"
fetch_scoop
echo "----------------------------------------"
fetch_brew
echo "----------------------------------------"
fetch_flatpak
echo "----------------------------------------"
fetch_nix
echo "----------------------------------------"
fetch_npm
echo "----------------------------------------"
fetch_pypi
echo "----------------------------------------"
fetch_cargo
echo "----------------------------------------"
fetch_helm
echo "----------------------------------------"
fetch_go
echo "----------------------------------------"
fetch_hackage
echo "----------------------------------------"


echo "========================================================"
echo "Metadata fetch process completed."
echo "All data has been saved in the '${OUTPUT_DIR}' directory."

