# Customer Experience Analytics for Fintech Apps


This directory contains the Exploratory Data Analysis (EDA) and data cleaning pipeline for customer reviews from Google Play Store for various Fintech companies suchas Commercial Bank of Ethiopia, Bank of Abyssinia (BOA), and Dashen Bank.

- **Goal:** to build a rigorous analytics pipeline that transforms raw Play Store reviews into actionable insights.

## Web Scraping Methodology
- **Method:** 
- **Target Period:** 2021 – 2026
- **Scraped reviews per Bank:** 
- **Limitations:** 

## 🛠️ Data Cleaning Pipeline
To ensure scientific accuracy, the following steps are performed in the `data_cleaner.py`:

1. **Null Handling:** Removal of Null values.
2. **date Conversion:** convert it to datetime format.



## 📊 Key Visualizations & Analysis
The analysis focuses on three core areas:
- **Charts:** 
- **Correlations:** 

## 📁 Repository Structure
- `notebooks/<company>_eda.ipynb`: Individual Company analysis notebooks.
- `data/<company>_clean.csv`: Cleaned output files (Note: Excluded from version control via `.gitignore`).

## 📚 References & Resources
- Web Scraping (Google Play Store)

PyPI Page
- GitHub Repository

Data Handling & Preprocessing

- 10 Minutes to pandas
- Working with Text Data – pandas
- Handling Missing Data – pandas

Sentiment Analysis & NLP

- Hugging Face Transformers – Sentiment Analysis Pipeline: 
- Model Card (distilbert-base-uncased-finetuned-sst-2-english)
- VADER Sentiment – GitHub
- TextBlob Quickstart

Thematic Analysis (Keyword Extraction & Topic Modeling)

- spaCy 101
- Scikit-learn TF-IDF (TfidfVectorizer)
- Scikit-learn LDA (LatentDirichletAllocation)
- Hugging Face Zero-Shot Classification
- Sentence Transformers Quickstart

Database (PostgreSQL)

- PostgreSQL Getting Started
- PostgreSQL Downloads
- psycopg2 Documentation: 
- SQLAlchemy PostgreSQL Dialect
- pgAdmin (GUI Tool)
- W3Schools SQL Tutorial
- PostgreSQL Tutorial

Unit Testing

- pytest Getting Started
- Python unittest – Basic Example
- A Gentle Introduction to Unit Testing in Python – Machine Learning Mastery
