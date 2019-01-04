# ATBS_S6_L14.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 14

# For Loop with lists, multiple assignments and Augmented operator

employee = ['John', 'manager', '2010']

print('\nindividual elements of the list using for loop')
for i in employee:
    print(i)

print('\nindividual elements of the list using for loop with range and index')
for i in range(len(employee)):
    print(employee[i])

print('\nprinting a list directly')
print(employee)

print('\nprinting a list with other string (converting from list to str)')
print('List is ' + str(employee))

print('\nmultiple assignment of the variables from a list')
empName, empDesignation, empJoiningYear = employee

print('\nprinting variables from multiple assignment from list \n'
      + empName + ' ' + empDesignation + ' ' + empJoiningYear)

print('\nprinting only variables')
print(empName, empDesignation, empJoiningYear)


print('\nExample of swap of Variables')
a = 123
b = 456
print('\na ' + str(a))
print('\nb ' + str(b))
a, b = b, a
print('\na ' + str(a))
print('\nb ' + str(b))

print('\nUsing augmented operator to increment index value'
      ' and printing list in while loop')

i = 0
while i < len(employee):
    print(str(i) + ': ' + str(employee[i]))
    i += 1
