# This is a  Centered Pyramid using Nested Loops

levels = int(input("How many levels? "))

for i in range(1, levels + 1):
    # Print leading spaces
    for j in range(levels - i):
        print(" ", end="")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    # Move to the next line
    print()