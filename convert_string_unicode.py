#!/usr/bin/python3

input_string = input("Enter a strign to hide: ")

secret_string = ""

for char in input_string:

    secret_string += str(ord(char) - 23)

print("Secret Message: ", secret_string)

input_string = ""
for i in range(0, len(secret_string)-1, 2):

    char_code = secret_string[i] + secret_string[i+1]

    input_string += chr(int(char_code) + 23)

print("Original Message", input_string)
