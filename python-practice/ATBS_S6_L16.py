# ATBS_S6_L16.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 16

# list, strings and list's mmutable (changed in place) vs string

# Lists data type is mmutable, it can be changed in place
# list variable is a pointer to the list in memory
# When you assign list variable to a new variables
# .. both point to same data in memoryview
# to make actual copy of the list use copy module
# import copy
# listname1 = copy.deepcopy(listnmae2)


# This function appends a value to the list passed to it
def appendToList(listVariableFunction):
    listVariableFunction.append("TheEnd")
    print('listVariableFunction', str(listVariableFunction))


# This is a list variable in main program
listVariableMainProgram = [1, 2, 3, 4, 5]

# We pass the list variable from main program to the function
appendToList(listVariableMainProgram)

# Since list variables are pointers,
# list pointed by  variable in main program is also modified by function
print('listVariableMainProgram', str(listVariableMainProgram))
