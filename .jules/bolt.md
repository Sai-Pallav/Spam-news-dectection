## 2024-10-13 - O(1) NLTK Stopwords Lookup Optimization
**Learning:** NLTK's `stopwords.words('english')` returns a list. Iterating through a dataset and checking membership for every token via `if not word in stopwords` results in an O(N) lookup for each word, severely bottlenecking NLP text preprocessing on large datasets.
**Action:** Always wrap `stopwords.words('english')` with `set()` (e.g., `set(stopwords.words('english'))`) to enable O(1) set membership lookups, which drastically reduces computational overhead during lemmatization and cleaning.
