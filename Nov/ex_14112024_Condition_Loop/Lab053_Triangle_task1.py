# ✅ Triangle Classifier:
#
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

# Step1 --> I/P ==float , O/P == String
side1 = float(input("Enter Side1 value"))
side2 = float(input("Enter Side2 value"))
side3 = float(input("Enter Side3 value"))

if side1 == side2 and side1 == side3:
    print("Equilateral Triangle")
elif side1 == side2 and side1 != side3:
    print("Isosceles Triangle")
elif side2 == side3 and side2 != side1:
    print("Isosceles Triangle")
elif side3 == side1 and side3 != side2:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
