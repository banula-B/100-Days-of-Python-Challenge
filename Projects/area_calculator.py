# This is a area calculator for different shapes

print("This is a Area Calculator")
print("Select Your Choice(Enter The Number Only")

print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Choice: "))

def calculate_rectangle(length, width):
    area = length* width
    print(f"Area of your rectangle: {area}")

def calculate_triangle(base,height):
    area = 0.5 * base * height
    print(f"Area of your rectangle: {area}")

def calculate_circle(radius, pi=3.14159):
    area = pi* radius**2
    print(f"Area of your rectangle: {area}")



if choice == 1:
    l = int(input("Enter Length: "))
    w = int(input("Enter Width: "))
    calculate_rectangle(length=l,width=w)

elif choice == 2:
    b = int(input("Enter Base: "))
    h = int(input("Enter Height: "))
    calculate_triangle(base=b, height=h)

elif choice == 3:
    r = int(input("Enter Radius: "))
    calculate_circle(radius=r)

else:
    print("Invalid Shape Selection")