# ATBS_S4_L11.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 4, Lecture 11

# try and except statements, bareback except, multiple except handle
# You dont want your program to crash when it gets error / exceptions
# So you try to execute, catch exceptions and then throw errors / handle errors
# Avoid using bareback except: as it will not give you correct trace
# example of bare back except Exception as e: print(e)
# Handling multiple exceptions in same way
#   except (e1, e2) as e:
#       steps to handle both e1 or e2
# Handling multiple exceptions independently
#   except e1 as err1:
#       steps to handle e1
#   except e2 as err2:
#       steps to handle e2

print('How many cars do you have?')
numcars = input()

try:
    if int(numcars) > 1:
        print('Do you really need that many cars?')
    else:
        print('Thats Ok')
except ValueError:
    print('Looks like you didnt enter a number')
