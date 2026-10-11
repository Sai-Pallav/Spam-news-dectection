## 2024-10-11 - [NLP Denial of Service (DoS) Risk in clean_row_dataset]
**Vulnerability:** The clean_row_dataset function in the ML Jupyter Notebooks processes potentially infinite length string inputs using computationally expensive operations like regular expressions and lemmatization.
**Learning:** Text input preprocessing functions intended for ML datasets often lack explicit boundaries, rendering applications using them susceptible to resource exhaustion if exposed to untrusted user input without length limits.
**Prevention:** Always sanitize inputs and enforce strict maximum string length limits inside data cleaning functions (e.g., limit inputs to 5000 characters) before running regex or NLP lemmatization.
