# ATBS_S1_L3.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 3

# Functions introduced or to practice
# input()
# using + in Print
# str()
# int()
# float()
# len()

print('Hi, what is your name?')
myName = input()

print('Hello ' + myName + '. Nice to meet you.')
print('Your name has ' + str(len(myName)) + ' charecters in it.\n')

print(myName + ', What is your age?')
# Converting to float to handle age like 5.5
# Then int will ignore the float age and just use integer part
myAge = int(float(input()))

if 0 < int(myAge) < 60:
    print('You will be 60 year old in ' + str(60 - int(myAge)) + ' years')
elif int(myAge) >= 60:
    print('I guess, you are never too old to learn programming right?')
elif int(myAge) == 0:
    print('I guess, you are just too young for coding')
else:
    print('Are you sure thats the right age?')
