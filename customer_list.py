#!/usr/bin/python3

#Create a list
customers = []

# Create a loop
while True:

    # Get input and make it work
    createEntry = input("Enter Customer (Yes/No): ")
    createEntry = createEntry[0].lower()

    #Check to leave loop
    if createEntry == 'n':
        break
    #Get customer data
    else:
        FirstName, LastName = input("Enter Customer Name: ").split()
        # Add customer data to list
        customers.append({'FirstName': FirstName, 'LastName': LastName})

# Print customer data
for cust in customers:
    print(cust['FirstName'], cust['LastName'])
