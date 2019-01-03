# ATBS_S3_L10.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 3, Lecture 10

# Global and local scopes of variables
# 1. Code in Global scope can not use local variables
# 2. Code in local scope can access global variables
#        (if there is no similar named local variable)
# 3. Code in one func's local scope cannot use variables from other local scope
# 4. You can use same name for diff variables if they are in diff local scopes
# How does python decides if a variable used in a function is local or global?
# If there is assignment statement for variable within function then it's local
# If there is no assignment then python considers it as global
# If you want to change value for a global variable within function then
#    declare it as Global variable using global keyword

# https://pythonspot.com/global-local-variables/
z = 10


def func1():
    global z
    z = 3


def func2(x, y):
    global z
    return x+y+z


func1()
total = func2(4, 5)

guess = int(input("Read the program guess the value of total \n"))

print('Your guess was: ' + str(guess))
print('Actual total is: ' + str(total))

if guess == total:
    print("Thats correct")
else:
    print("Thats Wrong")
