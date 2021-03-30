#!/usr/bin/python3

# Ask for the money invested + the interest rate
money = input("How much to invest : ")
interest_rate = input("Interest Rate : ")

# Convert value to a float and round the percentage rate by 2 digits.

money = float(money)
interest_rate = float(interest_rate) * .01

for i in range(10):
    money = money + (money * interest_rate)

print("Investment after 10 years : {:.2f}".format(money))
