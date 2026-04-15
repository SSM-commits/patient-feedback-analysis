from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
import os

print("🚀 Starting script...")

# Check file
if not os.path.exists("input/cleaned_feedback.csv"):
    print("❌ File NOT FOUND")
    exit()

spark = SparkSession.builder.appName("PatientFeedback").getOrCreate()
print("✅ Spark started")

df = spark.read.csv("input/cleaned_feedback.csv", header=True)

print("✅ Data loaded")
df.show()

# ✅ Sentiment WITHOUT UDF (IMPORTANT FIX)
df = df.withColumn(
    "sentiment",
    when(col("feedback").contains("good"), "Positive")
    .when(col("feedback").contains("excellent"), "Positive")
    .when(col("feedback").contains("bad"), "Negative")
    .when(col("feedback").contains("poor"), "Negative")
    .otherwise("Neutral")
)

print("✅ Sentiment added")
df.show()

# Saveoutput
df.toPandas().to_csv("data/processed_feedback.csv", index=False)
print("✅ Output saved!")