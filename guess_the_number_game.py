#!/usr/bin/python3

secret_number = 8

while True:
    guess = int(input("Please choose a numbert between 1 & 10: "))

    if guess == secret_number:
        print("You got it")
        break

