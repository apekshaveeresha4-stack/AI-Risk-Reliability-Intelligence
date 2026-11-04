from datasets import load_dataset

print("Starting dataset download...")

dataset = load_dataset("MothLabs/ai-incidents", split="train")

df = dataset.to_pandas()

df.to_csv("data/raw/ai_incidents_raw.csv", index=False)

print("DOWNLOAD SUCCESSFUL!")
print("Total records:", len(df))
print("Columns:", df.columns.tolist())
