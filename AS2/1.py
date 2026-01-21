def check_zander_size():
    length = int(input("Enter the length of the zander in centimeters: "))
    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print("Release the fish back into the lake.")
        print(f"The caught fish was {difference} centimeters below the size limit.")
    else:
        print("The zander meets the size limit and can be kept.")

# Main program
if __name__ == "__main__":
    check_zander_size()
