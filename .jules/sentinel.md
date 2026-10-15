## 2024-05-18 - NLP Denial of Service (DoS) in text processing
**Vulnerability:** Unbounded text input processing in machine learning preprocessing functions (`clean_row_dataset`).
**Learning:** Performing computationally expensive regex and lemmatization operations on arbitrarily large input strings can lead to excessive memory/CPU consumption, causing Denial of Service (DoS).
**Prevention:** Always enforce strict maximum string length limits and sanitize inputs before applying complex NLP transformations.
