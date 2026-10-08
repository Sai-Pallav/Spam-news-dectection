from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Make sure resources are available
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

ps = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
model = None
vectorizer = None

def load_models():
    global model, vectorizer
    if os.path.exists('logistic_model.pkl') and os.path.exists('tfidf_vectorizer.pkl'):
        model = joblib.load('logistic_model.pkl')
        vectorizer = joblib.load('tfidf_vectorizer.pkl')

def clean_text(text):
    text = str(text).lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    token = text.split()
    news = [ps.lemmatize(word) for word in token if not word in stop_words]
    return ' '.join(news)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or vectorizer is None:
        load_models()

    if model is None or vectorizer is None:
         return jsonify({'error': 'Model files not found. Please train the model first.'}), 500

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    news_text = data['text']
    cleaned_news = clean_text(news_text)

    transformed_news = vectorizer.transform([cleaned_news])

    prediction = model.predict(transformed_news)[0]

    # In the notebook: 0 means Real (Correct), 1 means Fake
    # Wait, in the notebook: real_news['label'] = 0, fake_news['label'] = 1

    is_real = bool(prediction == 0)

    # Also we could get probability but let's stick to predicting
    # Calculate simple confidence if available
    confidence = 0.0
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(transformed_news)[0]
        confidence = float(probabilities[0] if is_real else probabilities[1]) * 100

    return jsonify({
        'is_real': is_real,
        'label': 'REAL NEWS' if is_real else 'FAKE NEWS',
        'confidence': round(confidence, 2)
    })

if __name__ == '__main__':
    load_models()
    app.run(port=5000, debug=True)
