import re

def extract_dates(text):
    pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b'
    return re.findall(pattern, text)

# Example
text = "Meetings: 12/25/2023, 31-01-2024, January 1, 2023, 07/04/2022."
print(extract_dates(text))
