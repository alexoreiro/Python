#!/usr/bin/python3

# Swithc to lowercase for easy comparsion
def get_area(shape):

    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "square":
        square_area()
    elif shape == "triangle":
        triangle_area()
    else:
        print("Please enter square, rectangle, triangle or circle")

def rectangle_area():
    length = float(input("Enter the Length: "))
    width = float(input("Enter the Width: "))
    area = length * width

    print("The area of the rectangle is", area)

def square_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))
 
    area = length * width
 
    print("The area of the square is", area)

def circle_area():
    radius = float(input("Enter the radius: "))
     
    area = math.pi * (math.pow(radius, 2))
 
    print("The area of the circle is {:.2f}".format(area))
 
def triangle_area():
    
    # Three sides of the triangle is a, b and c:  
    a = float(input('Enter first side: '))  
    b = float(input('Enter second side: '))  
    c = float(input('Enter third side: '))  
  
    s = (a + b + c) / 2  
  
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
    print('The area of the triangle is %0.2f' %area)

def main():
    shape_type = input("Get area for what shape?: ")

    get_area(shape_type)

main()
