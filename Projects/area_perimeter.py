#This is for calculate area and perimeter of rectangle

print("Let's calculate the area and perimeter of a rectangle")

#Take length and width of rectangle from user

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


#formula for area and perimeter of rectangle

area = length * width
perimeter = 2 * (length + width)

print("Area: ", area)
print("Perimeter: ", perimeter)