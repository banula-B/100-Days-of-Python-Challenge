# This is program sort name list by last name

names = ["Lewis Hamilton", "Sebastian Vettel", "Charles Leclerc", "Max Verstappen", "Fernando Alonso"]

print(f"Original List: {names}")

names.sort(key=lambda name: name.split()[-1])

print(f"Sorted List: {names}")