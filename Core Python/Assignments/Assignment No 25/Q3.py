import re
from collections import Counter

def word_count(text):
    return dict(Counter(re.findall(r'\b\w+\b', text.lower())))

# Example
text = "This is a test. This test is simple!"
print(word_count(text))
