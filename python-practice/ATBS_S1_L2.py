
# ATBS_S1_L2.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 2
# It has some notes in comment form
# After that there is a section of Print statements
# First Print statement explains what next print statement will give demo of
'''
This is a muliline comment trick
https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python
'''

# This is a single line comment
# Python expects each comment to be separately commented with a single #
# Each editor provide a trick to select a block of text to comment or uncomment

# Expressions = Values + Operator
# Parenthesses
# Multiplication/Divisions first
# Addition / Subtraction second
# #
# Datatypes
# Integers
# Floats (Floating Point)
# Strings
# #
'''
This is a muliline comment trick
https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python
'''

print("Hello World!")

print("You can print extra enters or newlines using \\n \n")
print("Next line will print a Integer")
print(1, '\n')

print("Next line will print a Float")
print(1.0, '\n')

print("Next line will print a String")
print("THIS IS A String \n")

print("Next line will print output of expression 2 + 3 * 6, it should be 20")
print(2 + 3 * 6, '\n')

print("Next line will print output of expression (2 + 3) * 6, it should be 30")
print((2 + 3) * 6, '\n')

str_variable1 = "QA "
str_variable2 = "Trainee "
print("Next line will print output of a variable str_variable1 as String 1")
print("This is value stored in str_variable1: " + str_variable1)
print("This is value stored in str_variable2: " + str_variable2, '\n')

print("String can be added or concotinated")
print(str_variable1 + str_variable2 + '\n')

print("String can be not be deducted or multiplied \n")

print("But a string can be repeated a number of times as str_variable * 3 ")
print((str_variable1 + str_variable2 + '\n') * 3)
