# ATBS_S1_L8.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 8

# functions, random.randint(), sys.exit(), pip, pyperclip
# built in functions
# module: built in functions are written and grouped in modules
# you need to import modules
# import random
# this allows using randint() function as below
# random.randint(1,10)
# you can import multiple modules with columns
# you can use pip to install other 3rd party modules
# you can use pyperclip to access clipboard copy paste


# This program prints 10 random number
# If random number is 10 then it will exit from program
# also it will add the random number to your clipboard throughout the program

import random
import sys
import pyperclip

for i in range(1, 11):
    number = random.randint(1, 10)
    pyperclip.copy(number)
    print(number)
    if number == 10:
        print('Time to exit code')
        sys.exit()
