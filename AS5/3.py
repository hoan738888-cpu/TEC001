import re

def sum_numbers_in_text(text: str) -> int | float:
    numbers = re.findall(r'\d+\.?\d*', text)
    return sum(float(n) if '.' in n else int(n) for n in numbers)


text = input("Enter something:")
print(sum_numbers_in_text(text))