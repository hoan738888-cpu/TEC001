def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        numbers.append(int(user_input))

    numbers.sort(reverse=True)
    print("Five greatest numbers in descending order:")
    for num in numbers[:5]:
        print(num)

if __name__ == "__main__":
    main()
