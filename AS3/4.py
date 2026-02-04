def main():
    correct_user = "python"
    correct_pass = "rules"
    attempts = 0
    while attempts < 5:
        username = input("Username: ")
        password = input("Password: ")
        if username == correct_user and password == correct_pass:
            print("Welcome")
            return
        attempts += 1
        remaining = 5 - attempts
        if remaining > 0:
            print(f"Incorrect credentials. {remaining} attempts remaining.")
    print("Access denied")

if __name__ == "__main__":
    main()
