# Coronavirus Twitter Analysis (MapReduce)

## Project Summary

This project analyzes 1.1 billion geotagged tweets from 2020 to study how coronavirus-related hashtags spread across languages and countries worldwide.

Using a MapReduce-style parallel processing pipeline in Python, I processed large-scale compressed JSON data, extracted multilingual hashtag usage, and aggregated results by language and country. The system was designed to scale efficiently using Unix process control (`nohup`, background jobs) to parallelize daily tweet processing.

The final results were visualized using Matplotlib.

---

## What I Built

### 1. Scalable Data Pipeline
- Implemented a **MapReduce workflow** in Python
- Parsed compressed daily tweet archives (~1.1B tweets total)
- Extracted hashtag usage by:
  - Language (`lang`)
  - Country (`place.country_code`)
- Aggregated results across the entire year

### 2. Global Hashtag Analysis

The following visualizations were generated:

- `coronavirus_lang.png`  
  → Top 10 languages using **#coronavirus**

- `coronavirus_country.png`  
  → Top 10 countries using **#coronavirus**

- `korean_lang.png`  
  → Top 10 languages using **#코로나바이러스**

- `korean_country.png`  
  → Top 10 countries using **#코로나바이러스**

These plots show how COVID-related discussions differed geographically and linguistically across the world during 2020.

---

## Technical Skills Demonstrated

- Large-scale data processing
- MapReduce paradigm
- Parallel execution in Unix
- JSON parsing at scale
- Handling multilingual text
- Data aggregation
- Data visualization with Matplotlib
- Writing production-style Python scripts

---

## Why This Project Is Relevant

This project demonstrates my ability to design and implement scalable data systems that operate on billion-scale datasets. It mirrors real-world data engineering workflows used in industry, where efficiency, robustness, and clarity of analysis are critical.
