import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

ps = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def clean_row_dataset(row):
    row = str(row).lower()
    row = re.sub('[^a-zA-Z]', ' ', row)
    token = row.split()
    news = [ps.lemmatize(word) for word in token if not word in stop_words]
    return ' '.join(news)

def main():
    print("Loading data...")
    # Load dataset
    base_dir = "Spam News Detection - Logistic Regression"
    real_news = pd.read_csv(os.path.join(base_dir, 'true.csv'))
    fake_news = pd.read_csv(os.path.join(base_dir, 'fake.csv'))

    real_news['label'] = 0
    fake_news['label'] = 1

    dataset1 = real_news[['text', 'label']]
    dataset2 = fake_news[['text', 'label']]

    dataset = pd.concat([dataset1, dataset2])
    dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

    print("Cleaning text data... This may take a moment.")
    dataset['text'] = dataset['text'].apply(clean_row_dataset)

    # Use first 44898 rows as in original notebook
    n_samples = min(44898, len(dataset))
    X = dataset.iloc[:n_samples, 0]
    y = dataset.iloc[:n_samples, 1]

    print("Splitting dataset...")
    train_data, test_data, train_label, test_label = train_test_split(X, y, test_size=0.2, random_state=0)

    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(max_features=50000, lowercase=False, ngram_range=(1, 2))
    vec_train_data = vectorizer.fit_transform(train_data)
    vec_test_data = vectorizer.transform(test_data)

    print("Training Logistic Regression model...")
    classifier = LogisticRegression(random_state=42)
    classifier.fit(vec_train_data, train_label)

    print("Evaluating model...")
    y_pred_test = classifier.predict(vec_test_data)
    acc = accuracy_score(test_label, y_pred_test)
    print(f"Model Accuracy on Test Set: {acc:.4f}")

    print("Saving model and vectorizer...")
    joblib.dump(classifier, 'logistic_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    print("Done! Model saved to logistic_model.pkl and vectorizer to tfidf_vectorizer.pkl")

if __name__ == "__main__":
    main()
