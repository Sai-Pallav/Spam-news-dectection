## 2025-02-18 - Optimize Stopwords Lookup
**Learning:** Checking for membership in NLTK's `stopwords.words('english')` list is an O(N) operation per word, which significantly bottlenecks text preprocessing functions like `clean_row_dataset` when run over thousands of words in large datasets.
**Action:** Always convert stopword lists to a `set` (e.g., `set(stopwords.words('english'))`) for O(1) membership testing, which can yield >30x speedups in text cleaning functions.
