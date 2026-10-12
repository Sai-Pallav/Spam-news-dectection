## 2024-10-12 - Prevent NLP Denial of Service (DoS) in Notebook Preprocessing
**Vulnerability:** Unbounded user input in text preprocessing functions (`clean_row_dataset`) passed to computationally expensive operations like `re.sub` and NLTK lemmatization.
**Learning:** This repo lacked strict maximum string length limits in NLP text preprocessing, creating a severe memory/CPU DoS risk if given a massive payload.
**Prevention:** Always sanitize inputs and enforce strict maximum string length limits (e.g., `row = str(row)[:10000]`) inside preprocessing functions before applying computationally expensive regex or NLP operations.
