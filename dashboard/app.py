import streamlit as st
import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # add password if you set one
    database="hospital"
)

# Load data
df = pd.read_sql("SELECT * FROM feedback_analysis", conn)

st.title("🏥 Patient Feedback Dashboard")

# Sentiment distribution
st.subheader("Sentiment Distribution")
st.bar_chart(df['sentiment'].value_counts())

# Show full data
st.subheader("All Feedback Data")
st.write(df)