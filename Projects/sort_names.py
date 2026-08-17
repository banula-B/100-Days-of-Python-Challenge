# This is program sort name list by last name

names = ["Zoe Smith", "Alice Brown", "Charlie Davis", "Bob Miller"]

print(f"Original List: {names}")

names.sort(key=lambda name: name.split()[-1])

print(f"Sorted List: {names}")