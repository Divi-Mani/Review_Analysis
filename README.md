# Review Analysis (NLP Project)

This project uses **Natural Language Processing (NLP)** techniques to analyze customer reviews. It performs:

-  Text Summarization  
-  Sentiment Analysis  
-  Keyword Extraction

  The output is saved in a structured CSV file to help stakeholders understand key insights from customer feedback.

## Features
- **🔍 Text Summarization**  
  Condenses long customer reviews into short summaries using pre-trained NLP models.

- **😊 Sentiment Analysis**  
  Detects sentiment polarity (positive, negative, neutral) with a score between -1 (negative) to +1 (positive).

- **🏷️ Keyword Extraction**  
  Identifies key entities and terms using Named Entity Recognition (NER).

- **📁 CSV Output**  
  Creates a structured CSV file with:
  - Original Review  
  - Summarized Review  
  - Sentiment Score  
  - Extracted Keywords  


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
        `python code/review_analysis.py`
### 3.Output:
The script will print the results in the terminal and save them to a analysis_results.csv file in the root directory. The CSV will contain:

-Original Review

-Summarized Review

-Sentiment Score (from -1 to 1, where 1 is positive, -1 is negative, and 0 is neutral)

-Extracted Keywords

## Files and Functions
### 1. code/preprocess.py
Contains the preprocessing logic for cleaning and preparing the reviews. The reviews are tokenized, converted to lowercase, and stopwords are removed.

### 2. codr/review_analysis.py
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
