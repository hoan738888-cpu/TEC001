def remove_odds(numbers):
    return [n for n in numbers if n % 2 == 0]

# Testing
original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = remove_odds(original)

print("Original list:", original)
print("Filtered list:", filtered)
