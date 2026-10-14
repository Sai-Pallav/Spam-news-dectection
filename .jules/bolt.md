## 2024-10-14 - NLP Text Preprocessing Bottleneck
**Learning:** NLTK `stopwords.words('english')` returns a list, making the membership check (`word not in stopwords`) in list comprehensions during text preprocessing an O(N) operation per word. This causes severe bottlenecks on large text datasets.
**Action:** Always wrap `stopwords.words('english')` (or similar lists used for repeated lookups) with `set()` for O(1) membership lookup performance in NLP pipelines.
