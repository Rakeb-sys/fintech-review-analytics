# Customer Experience Analytics for Fintech Apps

This documentation outlines the systematic approach used to harvest the dataset, the temporal boundaries of the data, and the technical hurdles encountered during the execution of the project.

## 1. Data Scraping Methodology
  
  The extraction was conducted using the google_play_scraper, a Node.js-inspired Python library that retrieves data directly from the Google Play Store by mimicking HTTP requests to the store's internal APIs.

  Initialization: Targeted specific app_id values (e.g., com.example.app).

  Configuration: Set lang (language) and country (region) parameters to ensure data consistency, as Google Play content varies significantly by local.

  Sorting: Reviews were typically sorted by Sort.NEWEST to prioritize recent data

  Pagination: For high-volume apps, a loop was implemented to handle continuation_token objects, preventing data loss during transmission.

## 2. Date Range

    The data extraction was targeted for the following period:

    Start Date: 2025-02-21

    End Date: 2026-05-14

## 3. Limitations & Constraints

    During the scraping process, Date filtering was tried to performed. However google_play_scraper library does not support server-side date filtering. All reviews were scraped chronologically, and filtering will be performed post-extraction (locally).
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
