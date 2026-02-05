# dataset.py
# Multilingual Aksharantar Dataset Loader
# Auto Download + Offline Support

import json
import zipfile
import os
from huggingface_hub import hf_hub_download

# -----------------------------------
# Language Mapping
# -----------------------------------

LANG_PREFIX = {
    "hi": "hin",
    "bn": "ben",
    "ta": "tam",
}

DATA_DIR = "data"


# -----------------------------------
# Download or Load Local ZIP
# -----------------------------------

def get_zip_path(prefix):

    os.makedirs(DATA_DIR, exist_ok=True)

    local_path = os.path.join(DATA_DIR, f"{prefix}.zip")

    # Use local if exists
    if os.path.exists(local_path):
        print(f"Using local file → {local_path}")
        return local_path

    # Else download
    print(f"Downloading {prefix}.zip from HuggingFace...")

    zip_path = hf_hub_download(
        repo_id="ai4bharat/Aksharantar",
        filename=f"{prefix}.zip",
        repo_type="dataset"
    )

    return zip_path


# -----------------------------------
# Read ZIP Dataset
# -----------------------------------

def load_language_dataset(prefix):

    zip_path = get_zip_path(prefix)

    split_files = {
        "train": f"{prefix}_train.json",
        "validation": f"{prefix}_valid.json",
        "test": f"{prefix}_test.json",
    }

    data = {}

    with zipfile.ZipFile(zip_path, "r") as zf:

        for split, file_name in split_files.items():

            records = []

            with zf.open(file_name) as f:
                for line in f:
                    obj = json.loads(line.decode("utf-8"))

                    records.append({
                        "roman": obj["english word"],
                        "native": obj["native word"]
                    })

            print(f"{prefix} → {split}: {len(records)} samples")
            data[split] = records

    return data


# -----------------------------------
# Main Loader
# -----------------------------------

if __name__ == "__main__":

    for lang, prefix in LANG_PREFIX.items():

        print(f"\n==============================")
        print(f" Loading {lang.upper()} Dataset")
        print(f"==============================")

        data = load_language_dataset(prefix)

        print("\nSamples:\n")

        for i in range(5):
            print(
                data["train"][i]["roman"],
                "→",
                data["train"][i]["native"]
            )
