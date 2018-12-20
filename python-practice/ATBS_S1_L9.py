# ATBS_S1_L9.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 9

# user defined functions. optional parameters, return, none, sep, end in print
# user defined functions with optional parameters
# Python allows you to give default values for your parameters
# you can set default to blank if they are optional
# return values using return functions
# in lack of return statement python returns None value of None datatype
# in print statement there are parameters like sep=';' and end=''

# user defined functions with optional parameters


def hello_name(name=""):
    print('Hi ' + name)
    print('Hiiiii ' + name)
    print('Hiiiiiiiiii ' + name)
    print('\n')


hello_name()  # Uses default value "" when function is called
hello_name('QA')
hello_name('Trainee')
hello_name('QA-Trainee')


# function with a return statement
# This code asks user to enter a bill ammount
# it calculates tip at 10% and gives you total bill with tip


def tip(bill):
    return (bill * 0.1)


def billPlusTip(bill):
    return (bill + tip(bill))


print('What was your bill amount?')
bill = float(input())

print('For bill of rs ' + str(bill) +
      ' you need to pay tip of rs ' + str(tip(bill)) +
      ' which makes a total of rs ' + str(billPlusTip(bill)))
