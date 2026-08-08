# This is a marks manager with python lists

marks=[]

while True:
    user_input = input("Enter student marks (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    else:
        marks.append(float(user_input))

marks.sort(reverse=True)

print(f"Ranked marks are: {marks}")
print(f"Class Average is: {sum(marks)/len(marks):.2f}")
print(f"Highest Mark is: {marks[0]}")
print(f"Lowest Mark is: {marks[-1]}")