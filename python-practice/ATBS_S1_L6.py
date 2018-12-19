# ATBS_S1_L6.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 6

# while, break statement, continue statement

# break terminates the current loop and resumes execution at the next statement
# continue terminates the current loop iteration and resumes execution at the
# next iteration of current loop.

# while condition:
#     while statments

# Exercise for while
# print table of any integer upto 10, take the value of integer from user.

print('This program has 2 exercises')
print("Exercise 1: Enter an integer, this code will print its table: ")
number = int(float(input()))
i = 1

while (i <= 10):
    # print(number + ' * ' + i + ' = '  + (number * i))
    print(str(number) + ' * ' + str(i) + ' = ' + str(number * i))
    i = i + 1

# Exercise for break
# Ask user to enter a number and check if it is even number or not,
# Print result of even or odd and then continue asking for a new number
# Exit program if user enters Exit instead of number

print('\nExercise 2 : showing while, break and continue statements')

while True:
    print("\nEnter an integer, or type \'Exit'")
    number = input()
    if number == 'Exit':
        print('User entered \'Exit\'')
        print('Using the break statement, exiting from while loop and program')
        break
    elif number.isdigit():
            number = int(float(number))
            if number % 2 == 0:
                print(str(number) + ' is an even number')
            elif number % 2 != 0:
                print(str(number) + ' is an odd number')
            else:
                print(str(number) + ' this number is not handlled by code')
    else:
        print("That is not a valid input, enter an Integer or type \'Exit\'")
        print("Using the continue statement to receive a new input")
        continue
