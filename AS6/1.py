numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

numbers.sort(reverse=True)
print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)
