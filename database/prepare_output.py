import pandas as pd
import os

folder = "output/processed_feedback"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

df_list = []

for file in files:
    df_list.append(pd.read_csv(os.path.join(folder, file)))

df = pd.concat(df_list)

df.to_csv("data/processed_feedback.csv", index=False)

print("✅ Final CSV ready!")