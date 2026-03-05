import re

def redact_phone_numbers(text: str) -> str:
    pattern = r'\+84\d+|\b\d{10}\b'
    return re.sub(pattern, '[REDACTED]', text)

text = input("Enter something here:")
print(redact_phone_numbers(text))
