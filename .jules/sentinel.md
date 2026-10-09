## 2024-02-14 - NLP DoS Protection
**Vulnerability:** Machine learning data cleaning pipelines (regex and lemmatization) were vulnerable to NLP Denial of Service (DoS) due to unbounded input string lengths.
**Learning:** Python `re.sub` and NLTK `lemmatize` operations can consume excessive CPU time when processing extremely long strings, potentially causing a denial of service if processing untrusted user input or external datasets.
**Prevention:** Always enforce strict maximum string length limits (e.g., slicing to 10000 characters) before passing strings into computationally expensive NLP operations in `clean_row_dataset` or similar functions.
