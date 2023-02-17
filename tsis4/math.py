import math

#1
a = int(input("input degree: "))
x = a * math.pi / 180
print("output radian:", x)

#2
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
x = (b1 + b2) * h / 2
print("Area:", x)

#3
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
p = n * l
a = l / (2 * math.tan(180 / n))
area = p * a / 2
print("Area of the polygon is:", area)

#4
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
a = l * h
print("Area: ", a)