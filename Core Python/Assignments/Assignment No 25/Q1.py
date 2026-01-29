import re

def censor_text(text, forbidden_words):
    for word in forbidden_words:
        text = re.sub(rf'\b{re.escape(word)}\b', '*' * len(word), text, flags=re.IGNORECASE)
    return text

# Example
text = "This is a secret message. Do not share this confidential info."
forbidden_words = ["secret", "confidential"]
print(censor_text(text, forbidden_words))
