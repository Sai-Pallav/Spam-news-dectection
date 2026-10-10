## 2024-05-18 - Prevent NLP DoS with string length limits in data cleaning functions
**Vulnerability:** Machine learning data cleaning functions (e.g. `clean_row_dataset` for dataset generation and prediction) ran regex, split, and lemmatization on unbounded string input, exposing a Denial of Service (DoS) vulnerability (ReDoS/Algorithmic complexity attack).
**Learning:** External or user input must be sanitized and bounded before invoking computationally expensive operations in NLP pipelines.
**Prevention:** Always enforce strict maximum string length limits at the entry point of data cleaning or processing functions.
