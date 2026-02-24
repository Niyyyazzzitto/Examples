import math

# 1️ Convert degree to radian
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", round(radian, 6))


# 2️ Calculate the area of a trapezoid
height = float(input("\nHeight: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
trapezoid_area = (base1 + base2) * height / 2
print("Expected Output:", trapezoid_area)


# 3️ Calculate the area of a regular polygon
num_sides = int(input("\nInput number of sides: "))
side_length = float(input("Input the length of a side: "))
# Formula: (n * s^2) / (4 * tan(pi / n))
polygon_area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", round(polygon_area, 6))


# 4️ Calculate the area of a parallelogram
base = float(input("\nLength of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = base * height
print("Expected Output:", parallelogram_area)