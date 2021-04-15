#!/usr/bin/python3

# Problem: Receive miles and conver to kilometers

miles = input('Enter miles to be converted in km: ')
 
#kilometers = miles * 1.60934

miles = int(miles)

kilometers = miles * 1.60934

print("{} miles equals {} kilometers".format(miles, kilometers))
