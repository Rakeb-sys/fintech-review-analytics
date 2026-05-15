import re

import pandas as pd

def missing_values(df):
    print("Missing values per column:")
    print("-" * 30)
    print(df.isnull().sum())
    print("\nPercentage of missing values per column:")
    print("-" * 30) 
    print((df.isnull().mean() * 100).round(2))


def duplicate_reviews(df):
    print("Duplicate reviews:")
    print("-" * 30)
    duplicate_reviewId = df.duplicated(subset=['review_id'], keep=False)
    duplicate_count = duplicate_reviewId.sum()

    print(f"Total duplicate review IDs: {duplicate_count}")

    duplicate_review = df.duplicated(subset=['review'], keep=False)
    duplicate_count_review = duplicate_review.sum()
    print(f"Total duplicate review texts: {duplicate_count_review}")

    empty_review = df['review'].isnull().sum()
    print(f"Total empty reviews: {empty_review}")

    print(f"Total duplicate reviews: {duplicate_count}")
    if duplicate_count > 0:
        print("\nSample duplicate reviews:")
        print(df[duplicate_review].head())


def check_dateFormat(df):
    print("Checking date format:")
    print("-" * 30)
    print(f"Sample dates: {df['date'].iloc[0]}")
    print(f"Data type of 'date' column: {df['date'].dtype}")
    print(f"  Target format: YYYY-MM-DD (string or date object)")


def missing_values(df):
    before = len(df)
    # Drop rows missing the critical columns
    critical_cols = ['review', 'rating']
    df = df.dropna(subset=critical_cols)

    removed = before - len(df)
    print(f"Removed {removed} rows with missing critical data")
    print(f"Remaining: {len(df)} reviews")  
    return df

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates(subset=['review_id'])
    removed = before - len(df)
    print(f"Removed {removed} duplicate reviews based on review_id")
    print(f"Remaining: {len(df)} reviews")
    return df


def normalize_date(df):
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    print("Dates normalized to YYYY-MM-DD format")
    print(f"dtype: {df['date'].dtype}")
    print(f"\nDate range: {df['date'].min()} to {df['date'].max()}")
    return df



def clean_text(df, column='review'):
    """Standardize review text: collapse whitespace, strip edges."""
    df[column] = df[column].apply(lambda x: '' if pd.isna(x) else str(x))
    df[column] = df[column].str.strip()
    df[column] = df[column].str.replace(r'\s+', ' ', regex=True)
    return df


def invalid_reviews(df):
    # Check for out-of-range ratings that are not between 1 and 5
    invalid_ratings = df[(df['rating'] < 1) | (df['rating'] > 5)]
    print(f"Invalid ratings (outside 1–5): {len(invalid_ratings)}")
    
    df = df[(df['rating'] >= 1) & (df['rating'] <= 5)]
    print(f"Remaining reviews after removing invalid ratings: {len(df)}")
    df['rating'] = df['rating'].astype(int)
    print(f"Data type of 'rating' column: {df['rating'].dtype}")
    return df


def save_cleaned_data(cleaned_data, data_name):
    #save cleaned data to csv file
    cleaned_data.to_csv(f'../data/processed/cleaned_{data_name}.csv', index=True)

    #print the shape of the cleaned data
    print(f"Shape of cleaned {data_name}: {cleaned_data.shape}")

    #print the first 5 rows of the cleaned data
    print(f"First 5 rows of cleaned {data_name}:")
    print(cleaned_data.head())

    return cleaned_data

def preprocessing_report(df_raw, df_clean):
    print("=" * 55)
    print("  PREPROCESSING REPORT — Awash Bank Reviews")
    print("=" * 55)

    original_count = len(df_raw)
    final_count    = len(df_clean)
    removed_total  = original_count - final_count
    retention_rate = (final_count / original_count * 100)

    print(f"\n  Raw reviews collected  : {original_count:>6}")
    print(f"  Reviews after cleaning : {final_count:>6}")
    print(f"  Reviews removed        : {removed_total:>6}")
    print(f"  Data retention rate    : {retention_rate:>5.1f}%")

    quality = "EXCELLENT" if retention_rate >= 95 else ("GOOD" if retention_rate >= 90 else "NEEDS ATTENTION")
    print(f"  Data quality           : {quality}")

    print(f"\n  Date range : {df_clean['date'].min()}  to  {df_clean['date'].max()}")

    print("\n  Rating distribution:")
    for rating in sorted(df_clean['rating'].unique(), reverse=True):
        count = (df_clean['rating'] == rating).sum()
        pct   = count / final_count * 100
        bar   = '█' * (count // 5)
        print(f"    {rating} stars : {count:>4} ({pct:4.1f}%)  {bar}")

    print("\n  Text length stats:")
    lengths = df_clean['review'].str.len()
    print(f"    Min    : {lengths.min()} characters")
    print(f"    Median : {lengths.median():.0f} characters")
    print(f"    Max    : {lengths.max()} characters")

    print("\n  Columns in final CSV:")
    for col in df_clean.columns:
        print(f"    - {col}")

    print("\n" + "=" * 55)