#!/usr/bin/python3

i_string = input("Conver to Acronym: ")

i_string = i_string.upper()

list_of_words = i_string.split()

for word in list_of_words:
    print(word[0], end="")

print()
