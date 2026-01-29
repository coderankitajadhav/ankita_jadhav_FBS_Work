import re

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email))

# Example
emails = ["test@example.com", "invalid-email@", "user.name@domain.co"]
for e in emails:
    print(e, "->", is_valid_email(e))
