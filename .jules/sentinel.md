## 2024-10-08 - Added input length validation to prevent NLP DoS
**Vulnerability:** The data cleaning function in notebooks lacked length limits, creating a DoS risk if long strings were processed.
**Learning:** Text preprocessing steps using regex and lemmatization (like `clean_row_dataset`) can be CPU intensive. Without bounds checking, extremely long malicious inputs can exhaust resources.
**Prevention:** Always add maximum input length validation before heavy text manipulation algorithms.
