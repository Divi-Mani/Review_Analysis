# 📊 Review Analysis – NLP Project

This project uses **Natural Language Processing (NLP)** techniques to analyze customer reviews. It performs:

✅ Text Summarization  
✅ Sentiment Analysis  
✅ Keyword Extraction  

The output is saved in a structured CSV file to help stakeholders understand key insights from customer feedback.

---

##  Features

-  ** Text Summarization**  
  Condenses long customer reviews into short summaries using pre-trained NLP models.

-  ** Sentiment Analysis**  
  Detects sentiment polarity (positive, negative, neutral) with a score between -1 (negative) to +1 (positive).

-  ** Keyword Extraction**  
  Identifies key entities and terms using Named Entity Recognition (NER).

-  ** CSV Output**  
  Creates a structured CSV file with:
  - Original Review  
  - Summarized Review  
  - Sentiment Score  
  - Extracted Keywords  

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Review-Analysis-NLP-Project.git
cd Review-Analysis-NLP-Project
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Use

### 1. Prepare Input Data

- Create a file named `sample_reviews.txt` under the `data/` directory.
- Add customer reviews, one per line.

Example:

```
The product quality is excellent and delivery was super fast!
Terrible customer support. Would not recommend.
```

### 2. Run the Analysis Script

```bash
python code/review_analysis.py
```

### 3. Output

- The terminal will display the summarized analysis.
- Results will be saved in `analysis_results.csv` in the project root directory.

---

## Project Structure

```
Review-Analysis-NLP-Project/
│
├── code/
│   ├── preprocess.py           # Preprocessing logic (tokenization, stopword removal, etc.)
│   └── review_analysis.py      # Main script for summarization, sentiment, keywords
│
├── data/
│   └── sample_reviews.txt      # Sample customer reviews input
│
├── analysis_results.csv        # Auto-generated results (after running script)
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

---

## Dependencies

The key Python libraries used are:

- [`nltk`](https://www.nltk.org/) – Tokenization, stopword filtering  
- [`spacy`](https://spacy.io/) – Named Entity Recognition (NER)  
- [`transformers`](https://huggingface.co/transformers/) – Text summarization  
- [`textblob`](https://textblob.readthedocs.io/) – Sentiment analysis  
- [`pandas`](https://pandas.pydata.org/) – Dataframe handling & CSV export  

Install them via:

```bash
pip install -r requirements.txt
```

---
