# This is simple login system

username = "mala_admin"
password = "mala_admin123"

user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

if user_username == username and user_password == password:
    print("Login Successful! Welcome back.")
else:
    print("Invalid credentials. Please try again.")