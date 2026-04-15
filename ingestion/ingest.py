import pandas as pd
import os

print("🚀 Starting ingestion...")

# Check if file exists
file_path = "data/feedback.csv"
print("Looking for:", os.path.abspath(file_path))

if not os.path.exists(file_path):
    print("❌ feedback.csv NOT FOUND")
    exit()

# Load data
df = pd.read_csv(file_path)
print("✅ File loaded")

# Cleaning
df.dropna(inplace=True)
df['feedback'] = df['feedback'].astype(str).str.lower()

# Save cleaned file
output_path = "data/cleaned_feedback.csv"
df.to_csv(output_path, index=False)

print("✅ Saved at:", os.path.abspath(output_path))