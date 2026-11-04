import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/ai_incidents_cleaned.csv")

print("AI RISK ANALYSIS")
print("=" * 45)

# 1. Incidents by year
print("\n1. REPORTED INCIDENTS BY YEAR")
print(df["incident_year"].value_counts().sort_index())

# 2. Incidents by category
print("\n2. INCIDENTS BY CATEGORY")
print(df["category"].value_counts())

# 3. Incidents by severity
print("\n3. INCIDENTS BY SEVERITY")
print(df["severity"].value_counts())

# 4. High-risk incidents by category
print("\n4. HIGH-RISK INCIDENTS BY CATEGORY")
high_risk = df[df["high_risk_flag"] == True]
print(high_risk["category"].value_counts())

# 5. Classification confidence
print("\n5. CLASSIFICATION CONFIDENCE")
print("Category:", round(df["categoryConfidence"].mean(), 3))
print("Severity:", round(df["severityConfidence"].mean(), 3))

# 6. High-risk percentage
print("\n6. HIGH-RISK PERCENTAGE")
percentage = len(high_risk) / len(df) * 100
print(round(percentage, 2), "%")