import re
def is_valid_hex_color(color: str) -> str:
    match = re.match(r'^#[0-9A-Fa-f]{6}$', color)
    return 'TRUE' if match else 'FALSE'
color = input('Enter a color: ')
print(is_valid_hex_color(color))
