
import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/ai_incidents_raw.csv")

# 1. Dataset size
print("\n--- DATASET SHAPE ---")
print(df.shape)

# 2. Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 3. First five records
print("\n--- FIRST 5 RECORDS ---")
print(df.head())

# 4. Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 5. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 6. Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# 7. Most common incident categories

print("\n--- INCIDENT CATEGORIES ---")

print(df["category"].value_counts())

# 8. Severity distribution

print("\n--- SEVERITY DISTRIBUTION ---")

print(df["severity"].value_counts())

# 9. Most common AI developers

print("\n--- TOP AI DEVELOPERS ---")

print(df["developers"].value_counts().head(10))

# 10. Category and severity comparison

print("\n--- CATEGORY VS SEVERITY ---")

print(pd.crosstab(df["category"], df["severity"]))
