# Grade calculator based on marks using if, elif, else

# Get marks from user
marks = int(input("Enter your marks: "))

# Check marks and print grade
if marks >= 75:
    print("Grade A")
elif marks >= 65:
    print("Grade B")
elif marks >= 55:
    print("Grade C")
elif marks >= 35:
    print("Grade S")
else:
    print("Grade F")

    