import sqlite3
from pathlib import Path

db_path = Path("data/processed/ai_risk.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

queries = {
    "TOTAL RECORDS": """
        SELECT COUNT(*) FROM ai_incidents
    """,

    "SEVERITY DISTRIBUTION": """
        SELECT severity, COUNT(*)
        FROM ai_incidents
        GROUP BY severity
        ORDER BY COUNT(*) DESC
    """,

    "HIGH-RISK BY CATEGORY": """
        SELECT category, COUNT(*)
        FROM ai_incidents
        WHERE high_risk_flag = 1
        GROUP BY category
        ORDER BY COUNT(*) DESC
    """,

    "HIGH-RISK BY SOURCE": """
        SELECT source_group,
               COUNT(*),
               SUM(high_risk_flag),
               ROUND(100.0 * SUM(high_risk_flag) / COUNT(*), 2)
        FROM ai_incidents
        GROUP BY source_group
    """
}

for title, query in queries.items():

    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

connection.close()