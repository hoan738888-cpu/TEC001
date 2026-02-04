def main():
    smallest = None
    largest = None
    while True:
        s = input("Enter a number (empty to quit): ")
        if s == "":
            break
        try:
            num = float(s)
        except ValueError:
            print("Invalid number, try again.")
            continue
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    if smallest is None:
        print("No numbers were entered.")
    else:
        print(f"Smallest: {smallest}")
        print(f"Largest: {largest}")

if __name__ == "__main__":
    main()
