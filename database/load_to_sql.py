import pandas as pd
import mysql.connector

print("🚀 Loading CSV...")

# Load your processed data
df = pd.read_csv('data/processed_feedback.csv')
print("✅ CSV Loaded")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # <-- put your password here if you set one
    database="hospital"
)

cursor = conn.cursor()
print("✅ Connected to MySQL")

# Insert data
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO feedback_analysis (id, feedback, sentiment) VALUES (%s, %s, %s)",
        (int(row['id']), row['feedback'], row['sentiment'])
    )

conn.commit()
conn.close()

print("✅ Data inserted into MySQL!")