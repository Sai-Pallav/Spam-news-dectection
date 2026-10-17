## 2024-10-24 - [NLP DoS Prevention in Data Preprocessing]
**Vulnerability:** The `clean_row_dataset` function lacked input length validation before performing computationally expensive regex substitutions (`re.sub`) and stemming (`ps.stem`), making it vulnerable to NLP Denial of Service (DoS) attacks when processing excessively large input strings.
**Learning:** Even internal data processing pipelines or ML training scripts can be vulnerable to DoS if they process untrusted external data without bounds, especially when using regular expressions or complex NLP tokenization loops.
**Prevention:** Enforce strict maximum string length constraints (e.g., `row = str(row)[:10000]`) on all external text inputs *before* applying any NLP preprocessing steps.
