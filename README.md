# AI Risk & Reliability Intelligence System

## Project Overview

The AI Risk & Reliability Intelligence System is a data analytics project designed to explore AI-related incidents, vulnerabilities, research literature, and emerging risks.

The project uses Python, SQL, and Power BI to clean, classify, analyse, and visualize AI risk data.

## Problem Statement

As artificial intelligence adoption grows, understanding its potential risks and vulnerabilities becomes increasingly important.

This project analyses collected AI-related records to identify risk categories, severity patterns, source composition, and data quality limitations.

## Tools & Technologies

- Python – Data cleaning and preprocessing
- Pandas – Data manipulation and analysis
- SQLite – Database management
- SQL – Analytical queries
- Power BI – Interactive dashboards
- VS Code – Development environment

## Project Workflow

1. Collected the AI-related dataset.
2. Explored the dataset using Python.
3. Cleaned missing and invalid date records.
4. Created a high-risk indicator for HIGH and CRITICAL records.
5. Classified records into source groups.
6. Stored processed data in SQLite.
7. Performed analytical queries using SQL.
8. Created interactive dashboards using Power BI.

## Key Findings

- 8,759 records were analysed.
- 1,404 records were classified as HIGH or CRITICAL severity.
- LLM and DEEPFAKE categories had the largest high-risk record counts.
- Research literature represented the largest source group.
- Approximately 99.2% of records lacked sector information.
- The 2026 record volume was heavily influenced by research literature.

## Dashboard Pages

1. Executive Overview – Overall records, severity distribution, categories, and yearly trends.
2. Risk Insights – High-risk categories and severity patterns across source groups.
3. Data Quality & Sources – Source composition, top sources, and missing data analysis.

## Dataset

Source: [AI Incidents Dataset – Hugging Face](https://huggingface.co/datasets/MothLabs/ai-incidents)

## Important Data Limitations

The dataset combines incident reports, vulnerability disclosures, research literature, and other sources. It is not a complete census of real-world AI failures.

Record counts should not be interpreted as real-world incident rates. Severity classifications are dataset-provided and have not been independently verified. The large 2026 volume is influenced by research literature records.

## Project Objective

The objective is to demonstrate practical data analytics skills, including data cleaning, exploratory analysis, SQL querying, data visualization, and communicating analytical limitations.