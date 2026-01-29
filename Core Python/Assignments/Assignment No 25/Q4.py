import re

def extract_urls(text):
    return re.findall(r'https?://\S+|www\.\S+', text)

# Example
text = "Check out https://example.com and http://test.org or visit www.website.com."
print(extract_urls(text))
