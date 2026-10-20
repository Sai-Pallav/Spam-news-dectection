## 2024-05-18 - Optimize Stopwords Lookups in NLP Processing
**Learning:** In NLTK NLP preprocessing tasks (like those found in this codebase's spam detection models), looking up stopwords in lists (e.g., `word in stopwords.words('english')`) has O(N) complexity for every word.
**Action:** Convert NLTK stopword lists to Python sets (`set(stopwords.words('english'))`) to achieve O(1) time complexity for membership lookups, greatly speeding up dataset cleaning and preprocessing.
