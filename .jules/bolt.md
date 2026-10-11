## 2024-10-11 - Optimize NLTK Stopwords Lookup
**Learning:** Found an O(N) lookup bottleneck during NLP data preprocessing. The codebase was iterating over `stopwords.words('english')` (a list) for membership testing.
**Action:** Always convert standard NLP vocabulary/stopword lists into sets (`set(stopwords.words('english'))`) to achieve O(1) lookup performance during text cleaning loops.
