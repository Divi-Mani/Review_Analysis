import os
import pandas as pd
from textblob import TextBlob
import spacy
from transformers import pipeline
from preprocess import preprocess_text

# Load SpaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Text Summarization Pipeline
summarizer = pipeline("summarization")

# Function to perform text summarization
def summarize_review(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Function to perform aspect-based sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Function to extract keywords using SpaCy NER
def extract_keywords(text):
    doc = nlp(text)
    keywords = [ent.text for ent in doc.ents]
    return keywords

# Function to load reviews from file and preprocess them
def load_and_preprocess_reviews(file_path):
    with open(file_path, 'r') as file:
        reviews = file.readlines()

    processed_reviews = [preprocess_text(review) for review in reviews]
    return processed_reviews

# Main function to perform the analysis
def main():
    # Load and preprocess reviews
    file_path = 'data/sample_reviews.txt'
    reviews = load_and_preprocess_reviews(file_path)

    # Analyze each review
    results = []
    for review in reviews:
        # Summarize review
        summary = summarize_review(review)
        
        # Sentiment analysis
        sentiment = analyze_sentiment(review)
        
        # Keyword extraction
        keywords = extract_keywords(review)
        
        # Store results
        results.append({
            'review': review,
            'summary': summary,
            'sentiment': sentiment,
            'keywords': keywords
        })
    
    # Convert results to a DataFrame for easy viewing
    df = pd.DataFrame(results)
    print(df)
    
    # Optionally, save the results to a CSV file
    df.to_csv('analysis_results.csv', index=False)

if __name__ == '__main__':
    main()
