import re

def is_valid_course_code(code: str) -> bool:
    return bool(re.match(r'^[A-Z]{2,3}\d{3}$', code))
pattern = input('Enter a course code: ')
if is_valid_course_code(pattern):
    print('TRUE')
else:
    print('FALSE')

