

MODEL_NAME = "google/mt5-small"
OUTPUT_DIR = "ct2_mt5"

print("Run this command:\n")

print(f"""
ct2-transformers-converter ^
  --model {MODEL_NAME} ^
  --output_dir {OUTPUT_DIR}
""")
