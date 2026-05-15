from google_play_scraper import app, reviews, Sort
import pandas as pd


def scrape_metadata(app_id, bank):
    try: 
        app_info = app(
            app_id,
            lang='en',    # Language: English
            country='et'  # Country: Ethiopia
        )

        print("=" * 50)
        print(f"App Info for {bank}")
        print("=" * 50)
        print(f"App Title   : {app_info['title']}")
        print(f"Current Score: {app_info['score']}")
        print(f"Total Ratings: {app_info['ratings']:,}")
        print(f"Total Reviews: {app_info['reviews']:,}")
        print(f"Installs     : {app_info['installs']}")
        return app_info
    except Exception as ex:
        print(f"Error scraping metadata for {bank} app: {ex}")
        return None


def scrape_reviews(app_id, bank, count):
    try:
        result, continuation_token = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,       # Most recent first
        count=count,              # Ask for more than 400 to be safe
        filter_score_with=None  # All star ratings
        )

        print(f"Collected {len(result)} raw reviews for {bank} app.")
        df_reviews = pd.DataFrame(result)
        return df_reviews, continuation_token
    
    except Exception as ex:
        print(f"Error scraping reviews for {bank} app: {ex}")
        return pd.DataFrame(), None
    

    

def data_quality_check(df):
    print("Data Quality Check:")
    print("-" * 30)
    print(f"Total reviews collected: {len(df)}")
    print(f"Missing values per column:\n{df.isnull().sum()}")