## 2024-05-18 - Avoid dense matrices for TF-IDF in NLP
**Learning:** Converting sparse matrices (like the output of TfidfVectorizer) to dense representations using `.toarray()` or wrapping them in pandas DataFrames causes severe memory OOM bottlenecks, especially with large vocabularies (e.g., 50,000 features) in text classification tasks.
**Action:** Always pass sparse matrices directly to scikit-learn models without converting them to dense arrays or pandas DataFrames.
