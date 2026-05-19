conn = psycopg2.connect(
    host="localhost",
    database="bank_reviews",
    user=user,
    password=password
)

CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_code VARCHAR(10) UNIQUE,
    bank_name VARCHAR(255),
    app_name VARCHAR(255)
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score NUMERIC,
    identified_theme VARCHAR(50),
    source VARCHAR(50)
);