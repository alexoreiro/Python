#!/usr/bin/python3

# Scalene triangle: All sides have different lengths.
# Isosceles tirangle: Two sideshave the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of the side a = "))
b = int(input("The length of the side b = "))
c = int(input("The length of the side b = "))

if a != b and b != c and a != c:
    print("This is a Scalene triangle.")
elif a == b and b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")
