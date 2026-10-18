## 2023-10-18 - Prevent NLP DoS in Jupyter notebooks
**Vulnerability:** Found `clean_row_dataset` taking unsanitized user inputs through potentially unbounded string lengths for costly regex replacement and lemmatization operations, opening up risks of NLP DoS.
**Learning:** Text preprocessing pipelines in machine learning notebooks can often be subjected to Denial of Service bottlenecks without string truncation boundaries.
**Prevention:** Always sanitize text inputs in ML pipelines, specifically by enforcing strict maximum string length limits to cap computationally expensive text transformations (like regex or lemmatization).
