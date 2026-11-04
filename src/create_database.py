import pandas as pd
import sqlite3
from pathlib import Path

# Load classified dataset
df = pd.read_csv(
    "data/processed/ai_incidents_classified.csv"
)

# Create database folder
db_path = Path("data/processed/ai_risk.db")

# Connect to SQLite database
connection = sqlite3.connect(db_path)

# Load dataset into SQL table
df.to_sql(
    "ai_incidents",
    connection,
    if_exists="replace",
    index=False
)

# Verify database
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM ai_incidents")
total_records = cursor.fetchone()[0]

print("DATABASE CREATED SUCCESSFULLY!")
print("Total records:", total_records)

cursor.execute("PRAGMA table_info(ai_incidents)")
print("\nDATABASE COLUMNS:")

for column in cursor.fetchall():
    print(column[1])

connection.close()