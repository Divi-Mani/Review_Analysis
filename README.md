# Review Analysis (NLP Project)

This project leverages Natural Language Processing (NLP) techniques to analyze customer reviews. It includes text summarization, aspect-based sentiment analysis, and keyword extraction. The goal is to extract meaningful insights from user feedback and provide structured summaries for easy understanding.

## Features
- **Text Summarization:** Condenses lengthy customer reviews into concise summaries.
- **Sentiment Analysis:** Analyzes the sentiment (positive/negative/neutral) expressed in reviews.
- **Keyword Extraction:** Extracts relevant keywords from reviews using Named Entity Recognition (NER).
- **CSV Output:** Generates a structured CSV file with summaries, sentiment scores, and keywords for each review.


## Installation

### 1. Clone the repository
      git clone https://github.com/yourusername/Review-Analysis-NLP-Project.git
      cd Review-Analysis-NLP-Project

### 2. Set up a virtual environment
      python -m venv venv
      source venv/bin/activate   # On Windows, use venv\Scripts\activate

### 3.Install required dependencies
      pip install -r requirements.txt

## How to Use:

### 1.Data Preparation:
  Place your customer reviews in a text file (sample_reviews.txt) in the data/ directory. Each review should be on a new line.
  
### 2. Run the Analysis:
  To start the review analysis, execute the following command:
        `python src/review_analysis.py`
### 3.Output:
The script will print the results in the terminal and save them to a analysis_results.csv file in the root directory. The CSV will contain:

-Original Review

-Summarized Review

-Sentiment Score (from -1 to 1, where 1 is positive, -1 is negative, and 0 is neutral)

-Extracted Keywords

## Files and Functions
### 1. src/preprocess.py
Contains the preprocessing logic for cleaning and preparing the reviews. The reviews are tokenized, converted to lowercase, and stopwords are removed.

### 2. src/review_analysis.py
The main script for:

-Summarizing reviews.

-Performing sentiment analysis.

-Extracting keywords.

-Generating and saving the analysis results.
### 3. data/reviews.txt
A sample file with customer reviews. You can replace this file with your own dataset.
### 4. requirements.txt
This file contains the Python dependencies required to run the project. The key libraries are:
-nltk

-spacy

-transformers

-pandas

-textblob
