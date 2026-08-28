class UsernameTooShortError(Exception):
    pass

class PasswordTooWeakError(Exception):
    pass


def username_validation(username):
    if len(username) < 5:
        raise UsernameTooShortError(
            "Username must be at least 5 characters long! "
        )
    print("Username is valid")   

def password_validation(password):
    special_characters = "!@#$%^&*"
    has_special_character = any(char in special_characters for char in password)

    if len(password) < 8 or not has_special_character:
        raise PasswordTooWeakError(
            "Password must be at least 8 characters long "
            "and contain at least one special character (!@#$%^&*)"
        )
    print("Password is valid")    

username = input("Enter Username:")
password = input("Enter Password:")

valid_username = False
valid_password = False

try:
    username_validation(username)
    valid_username = True
except UsernameTooShortError as e:
    print(f"Error: {e}")

try:
    password_validation(password)
    valid_password = True
except PasswordTooWeakError as e:
    print(f"Error: {e}")

if valid_username and valid_password:
    print(
        "Credentials valid!\n"
        "Account successfully created."
    )

