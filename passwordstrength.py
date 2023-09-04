import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase letters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\-]', password):
        return False

    # If all checks pass, the password is considered strong
    return True

def main():
    password = input("Enter a password to check its strength: ")
    if is_strong_password(password):
        print("Strong password!")
    else:
        print("Weak password. Please make it stronger.")

if __name__ == "__main__":
    main()
