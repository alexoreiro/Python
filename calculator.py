# Enter Calculation:
# 5 + 6 = 30

# Store the user input of 2 numbers and the operator

num1, operator, num2 = input('Enter Calculation ').split()

# Convert the string into integer

num1 = int(num1)
num2 = int(num2)

# if  + then we need to provide the output based on addition
# Print the result

if operator == "+":
    print("{} + {} = {}".format(num1,num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1,num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1,num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1,num2, num1 / num2))
else:
    print("Use either + - * or / next time")
