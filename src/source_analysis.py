import pandas as pd

df = pd.read_csv("data/processed/ai_incidents_cleaned.csv")

# Identify arXiv records
df["is_arxiv"] = (
    df["sourceName"].str.contains("arxiv", case=False, na=False)
)

print("=" * 50)
print("SOURCE QUALITY ANALYSIS")
print("=" * 50)

# 1. ArXiv vs other sources
print("\n1. SOURCE GROUPS")

print(
    df["is_arxiv"]
    .value_counts()
    .rename(index={True: "arXiv", False: "Other sources"})
)

print("\nPercentage of dataset:")
print(
    (df["is_arxiv"].value_counts(normalize=True) * 100).round(2)
)

# 2. Severity comparison
print("\n2. SEVERITY: ARXIV VS OTHER SOURCES")

print(
    pd.crosstab(
        df["is_arxiv"],
        df["severity"],
        normalize="index"
    ).round(3) * 100
)

# 3. Category comparison
print("\n3. CATEGORY: ARXIV VS OTHER SOURCES")

print(
    pd.crosstab(
        df["is_arxiv"],
        df["category"]
    )
)

# 4. Top sources overall
print("\n4. TOP 15 SOURCES")

print(df["sourceName"].value_counts().head(15))

# 5. High-risk percentages by source group
print("\n5. HIGH-RISK PERCENTAGE BY SOURCE GROUP")

print(
    df.groupby("is_arxiv")["high_risk_flag"]
    .mean()
    .mul(100)
    .round(2)
)