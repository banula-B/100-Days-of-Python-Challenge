# This is a project for multiplication table

# Get user input
num = int(input("Enter a number: "))

# Generate multiplication table
for i in range(1,11):
    print(num ,"x" , i , "=", num * i)

# Since we have not learned about formatted strings yet, we are using this method.