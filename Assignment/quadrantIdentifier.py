# Quadrant Identifier: Write a Python program that takes the coordinates (x, y) of
# a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or 4th).

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

if x > 0 and y > 0:
    print("The point is in the 1st Quadrant.")
elif x < 0 and y > 0:
    print("The point is in the 2nd Quadrant.")
elif x < 0 and y < 0:
    print("The point is in the 3rd Quadrant.")
elif x > 0 and y < 0:
    print("The point is in the 4th Quadrant.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point is on the y-axis.")
elif y == 0:
    print("The point is on the x-axis.")