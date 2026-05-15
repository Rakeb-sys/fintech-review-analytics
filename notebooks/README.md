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