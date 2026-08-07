# This is shopping list using python lists

shopping_list = []

while True:
    user_input = input("Add item: ")
    if user_input.lower() == "done":
        break
    shopping_list.append(user_input)

print("\n Your Final Shopping List: ")

for item in shopping_list:
    print("-", item)