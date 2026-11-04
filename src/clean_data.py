
import pandas as pd
from pathlib import Path

# Load original dataset
df = pd.read_csv("data/raw/ai_incidents_raw.csv")

print("Original dataset:", df.shape)

# Remove columns with no useful analytical value
df = df.drop(columns=["location", "imageUrl"])

# Convert date columns
date_columns = ["dateOccurred", "datePublished", "dateIngested"]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)

# Remove records without an occurrence date
df = df.dropna(subset=["dateOccurred"])

# Remove duplicate IDs, keeping the first record
df = df.drop_duplicates(subset=["id"])

# Create a high-risk flag
df["high_risk_flag"] = df["severity"].isin(
    ["HIGH", "CRITICAL"]
)

# Create a year column
df["incident_year"] = df["dateOccurred"].dt.year

# Save cleaned data
output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)

df.to_csv(output_path / "ai_incidents_cleaned.csv", index=False)

print("\nCLEANING COMPLETED")
print("Cleaned dataset:", df.shape)
print("High-risk records:", df["high_risk_flag"].sum())
print("Saved successfully!")
