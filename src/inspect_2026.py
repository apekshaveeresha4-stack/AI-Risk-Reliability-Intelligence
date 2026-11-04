import pandas as pd

df = pd.read_csv("data/processed/ai_incidents_cleaned.csv")

df["dateOccurred"] = pd.to_datetime(
    df["dateOccurred"], errors="coerce", utc=True
)

# Filter 2026 records
data_2026 = df[df["dateOccurred"].dt.year == 2026]

print("TOTAL 2026 RECORDS:", len(data_2026))

# Inspect a sample of 15 records
print("\nSAMPLE OF 2026 INCIDENTS")
print("=" * 70)

sample = data_2026.sample(
    n=min(15, len(data_2026)),
    random_state=42
)

for _, row in sample.iterrows():
    print("\nTitle:", row["title"])
    print("Date:", row["dateOccurred"])
    print("Category:", row["category"])
    print("Severity:", row["severity"])
    print("Source:", row["sourceName"])
    print("Summary:", str(row["summary"])[:250])
    print("-" * 70)

# Check the most common sources
print("\nTOP 15 SOURCES IN 2026")
print(data_2026["sourceName"].value_counts().head(15))

# Compare source counts across years
print("\nTOP SOURCES: 2025")
print(
    df[df["dateOccurred"].dt.year == 2025]
    ["sourceName"].value_counts().head(10)
)