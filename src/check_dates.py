import pandas as pd

df = pd.read_csv("data/processed/ai_incidents_cleaned.csv")

date_columns = ["dateOccurred", "datePublished", "dateIngested"]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)

    print("\n" + "=" * 45)
    print("DATE COLUMN:", col)
    print("=" * 45)

    print("Earliest date:", df[col].min())
    print("Latest date:", df[col].max())

    print("\nRecords by year:")
    print(df[col].dt.year.value_counts().sort_index())

    print("\nLatest 10 dates:")
    print(df[col].sort_values(ascending=False).head(10))