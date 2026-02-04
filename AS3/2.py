def main():
    while True:
        s = input("Enter inches : ")
        try:
            inches = float(s)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if inches < 0:
            print("Goodbye!")
            break
        cm = inches * 2.54
        print(f"{inches} in = {cm:.2f} cm")

if __name__ == "__main__":
    main()
