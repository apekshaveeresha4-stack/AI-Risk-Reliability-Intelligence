import pandas as pd

df = pd.read_csv("data/processed/ai_incidents_cleaned.csv")

# Classify records by source
def classify_source(source):

    source = str(source).lower()

    if "arxiv" in source:
        return "Research Literature"

    elif "ai incident database" in source:
        return "Incident Database"

    elif "nvd cve" in source:
        return "Vulnerability Disclosures"

    else:
        return "Other Sources"


df["source_group"] = df["sourceName"].apply(classify_source)

# Display source group counts
print("\nSOURCE GROUP DISTRIBUTION")
print("=" * 45)

print(df["source_group"].value_counts())

# Compare severity across source groups
print("\nSEVERITY DISTRIBUTION BY SOURCE GROUP")
print("=" * 45)

print(
    pd.crosstab(
        df["source_group"],
        df["severity"],
        normalize="index"
    ).round(3) * 100
)

# Calculate high-risk percentage
print("\nHIGH-RISK PERCENTAGE BY SOURCE GROUP")
print("=" * 45)

print(
    df.groupby("source_group")["high_risk_flag"]
    .mean()
    .mul(100)
    .round(2)
)

# Save classified dataset
df.to_csv(
    "data/processed/ai_incidents_classified.csv",
    index=False
)

print("\nClassified dataset saved successfully!")