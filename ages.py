# Enter your age

age = eval(input('What is your age? '))

if (age >= 1) and (age <= 18):
    print('You should be studing')
elif (age >= 19) and (age <= 75):
    print('You should be working')
elif (age > 75):
    print('you should be retired')

