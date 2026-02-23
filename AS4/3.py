def main():
    cities = []
    for i in range(5):
        city = input(f"Enter city {i+1}: ")
        cities.append(city)

    print("You entered these cities:")
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()
