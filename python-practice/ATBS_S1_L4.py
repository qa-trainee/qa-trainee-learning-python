# ATBS_S1_L4.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 4

# introduced or to practice
# Bollean values can be only True or False
# Comparison operators
# ==, !=, <, >, <=, >=
# Boolean operators
# and, or, not
# Concepts of Truth table for and, or, not
# True and True = True


# Excercise: Take users age as input and write a print statment that gives
# output of Bollean values for age comparison with 60 age

print('Enter your age:')
age = int(float(input()))

print('You are less than 60 year old? ' + str(age < 60))
print('You are more than 60 year old? ' + str(age > 60))
print('You are 60 year old? ' + str(age == 60))
print('You are not 60 year old? ' + str(age != 60))
