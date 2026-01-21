def hemoglobin_check():
    sex = input("Enter your biological sex (male/female): ").lower()
    value = int(input("Enter your hemoglobin value : "))
    print(value,"g/l")
    if sex == "female":
        if value < 117:
            print("Hemoglobin value is low.")
        elif value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif sex == "male":
        if value < 134:
            print("Hemoglobin value is low.")
        elif value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid input for biological sex.")
# Main program
if __name__ == "__main__":
    hemoglobin_check()