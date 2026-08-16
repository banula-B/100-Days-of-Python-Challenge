is_valid = False

def check_length(password):
    if len(password) >= 8:
        return True

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True

def validate_password():

    global is_valid

    password = input("Enter your password: ")

    if check_length(password) == True and check_digit(password) == True:
        is_valid = True
        print("Password is valid")
    else:
        print("Password is not valid")

validate_password()

if is_valid == True:
    print("System unlocked")
else:
    print("System locked")