## 2024-05-15 - NLP Denial of Service (DoS) via Unbounded Input Length
 **Vulnerability:** The `clean_row_dataset` function processes text using expensive operations (regex, tokenization, lemmatization) without limiting input length, opening the system up to NLP Denial of Service (DoS) if deployed to a backend.
 **Learning:** In early-stage machine learning notebooks, data preprocessing is often optimized for batch processing on clean datasets rather than defensive handling of potentially adversarial, unbounded strings.
 **Prevention:** Always enforce strict maximum string length constraints at the boundary of any NLP preprocessing pipeline to mitigate worst-case CPU scaling limits.
