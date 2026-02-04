def middle_chars(s: str) -> str:
    """Return the middle character for odd-length strings, or middle two for even-length."""
    if not s:
        return ""
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    else:
        return s[mid-1:mid+1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(middle_chars(s))