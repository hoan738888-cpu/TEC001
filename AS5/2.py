import re
def is_valid_hex_color(color: str) -> bool:
    return bool(re.match(r'^#[0-9A-Fa-f]{6}$', color))
color  = input('Enter a color: ')
if is_valid_hex_color(color)    :
    print("TRUE")
else:
    print("FALSE")
