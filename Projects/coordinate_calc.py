# This is a Coordinate Calculator

# Storing the coordinates

point_a = (2,4)
point_b = (8,10)

# Unpack coordinates

x1,y1 = point_a
x2,y2 = point_b

#calculate the manhattan distance

distance = abs(x1-x2) + abs(y1-y2)

print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print(f"The Manhattan Distance between the points is: {distance}")