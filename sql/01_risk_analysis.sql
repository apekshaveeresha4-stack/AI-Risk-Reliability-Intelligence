
-- ==========================================
-- AI RISK & RELIABILITY INTELLIGENCE SYSTEM
-- SQL ANALYSIS
-- ==========================================

-- QUERY 1: Total number of records
SELECT COUNT(*) AS total_records
FROM ai_incidents;


-- QUERY 2: Severity distribution
SELECT
    severity,
    COUNT(*) AS total_records
FROM ai_incidents
GROUP BY severity
ORDER BY total_records DESC;


-- QUERY 3: High-risk records by category
SELECT
    category,
    COUNT(*) AS high_risk_records
FROM ai_incidents
WHERE high_risk_flag = 1
GROUP BY category
ORDER BY high_risk_records DESC;


-- QUERY 4: High-risk percentage by source group
SELECT
    source_group,
    COUNT(*) AS total_records,
    SUM(high_risk_flag) AS high_risk_records,
    ROUND(
        100.0 * SUM(high_risk_flag) / COUNT(*), 2
    ) AS high_risk_percentage
FROM ai_incidents
GROUP BY source_group
ORDER BY high_risk_percentage DESC;


-- QUERY 5: Yearly record distribution
SELECT
    incident_year,
    COUNT(*) AS total_records
FROM ai_incidents
GROUP BY incident_year
ORDER BY incident_year;


-- QUERY 6: Category and severity comparison
SELECT
    category,
    SUM(CASE WHEN severity = 'CRITICAL' THEN 1 ELSE 0 END)
        AS critical_records,
    SUM(CASE WHEN severity = 'HIGH' THEN 1 ELSE 0 END)
        AS high_records,
    SUM(CASE WHEN severity IN ('HIGH', 'CRITICAL') THEN 1 ELSE 0 END)
        AS high_risk_records
FROM ai_incidents
GROUP BY category
ORDER BY high_risk_records DESC;


-- QUERY 7: Average classification confidence
SELECT
    ROUND(AVG(categoryConfidence), 3)
        AS avg_category_confidence,
    ROUND(AVG(severityConfidence), 3)
        AS avg_severity_confidence
FROM ai_incidents;


-- QUERY 8: Top 10 reporting sources
SELECT
    sourceName,
    COUNT(*) AS total_records
FROM ai_incidents
GROUP BY sourceName
ORDER BY total_records DESC
LIMIT 10;
