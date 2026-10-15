## 2024-05-18 - [Optimize NLP Text Preprocessing with Sets]
**Learning:** In Python NLP preprocessing, looking up stopwords in an NLTK list (O(N)) during list comprehensions over millions of words is a major bottleneck.
**Action:** Always convert NLTK stopwords lists to Python sets (e.g., `set(stopwords.words('english'))`) for O(1) lookup performance to drastically speed up text cleaning.
