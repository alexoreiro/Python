#!/usr/bin/python3

factorial = input("Enter the number to factorize: ")

def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num -1)
        return result
fact = result
print("This is the result", fact)


