import re
def is_valid_course_code(code: str) -> str:
    match = re.match(r'^[A-Z]{2,3}\d{3}$', code)
    return 'TRUE' if match else 'FALSE'
pattern = input('Enter a course code: ')
print(is_valid_course_code(pattern))
