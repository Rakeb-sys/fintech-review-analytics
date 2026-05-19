📊 KAIM - Customer Experience Analytics for Fintech Apps

📌 Overview

This project is designed for scalable Python-based Sentiment analysis and Correlation Analysis, combining data cleaning, exploratory data analysis (EDA), and reproducible workflows.

It includes:

Structured source code (src/) Interactive analysis via notebooks (notebooks/) Automated testing (tests/) Utility scripts (scripts/) CI/CD integration via GitHub Actions

The goal is to to conduct a rigorous, two-fold analysis of the scraped dataset from google play store that transforms raw Play Store reviews into actionable insights: quantifying sentiment, identifying recurring themes, and translating them into concrete recommendations that bank product teams can act on.

🗂️ Project Structure :
fintech-review-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   └── raw/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md


⚙️ Setup Instructions

Create and activate a virtual environment python -m venv .venv Windows .venv\Scripts\activate Linux / macOS source .venv/bin/activate
Install dependencies pip install -r requirements.txt
📊 Exploratory Data Analysis (EDA) 🔹 How to Run Start Jupyter Notebook: jupyter notebook Navigate to: notebooks/ Open the EDA notebook (e.g., analysis.ipynb) and run all cells. 🔹 Analysis Workflow


📁 Outputs

Generated outputs are organized as follows:

📌 Cleaned Data data/_clean.csv

⚠️ The data/ directory is excluded from version control via .gitignore.

⚡ER Diagram of DB:
banks
-----
bank_id (PK)
bank_code
bank_name
app_name

        1
        │
        │
        ▼
reviews
-------
review_id (PK)
bank_id (FK)
review_text
rating
review_date
sentiment_label
sentiment_score
identified_theme
source

🗄️ Database Schema
1. Banks table
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_code VARCHAR(10) UNIQUE NOT NULL,
    bank_name VARCHAR(255) UNIQUE NOT NULL,
    app_name VARCHAR(255)
);

2. Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT NOT NULL,
    review_text TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score NUMERIC(10,6),
    identified_theme VARCHAR(50),
    source VARCHAR(50),

    CONSTRAINT fk_bank
        FOREIGN KEY (bank_id)
        REFERENCES banks(bank_id)
        ON DELETE CASCADE
);

🔗 Relationship 

banks (1) ──────── (many) reviews


✔ Primary Keys
banks.bank_id
reviews.review_id

✔ Foreign Key
reviews.bank_id → banks.bank_id


📊 Visualizations

Stored (optionally) in:

reports/figures/ 📝 Reports

Analysis summaries can be stored in(not currently available):

reports/ 🧪 Running Tests

Run unit tests with:

pytest

Tests are automatically executed in CI via:

.github/workflows/unittests.yml

🤖 Automation Scripts

Scripts in scripts/ can be used for:

Data preprocessing Batch execution of analysis Pipeline automation

Run a script:

python scripts/<script_name>.py


