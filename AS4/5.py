def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    filtered_list = remove_odds(my_list)
    print("Original list:", my_list)
    print("Even numbers only:", filtered_list)

if __name__ == "__main__":
    main()
