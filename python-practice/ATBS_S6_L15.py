# ATBS_S6_L15.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 15

# Methods, List methods
# Datatypes in python have different methods that you can use on the variable
# list has index, add, drop, del methods
# Methods are tied to the datatypes, for ex: you can use list methods ons str

emp1 = ['John', 'QA', '2010']
emp2 = ['Jack', 'DEV', '2013']

print('Find the index for string from a list')
print(emp1.index('QA'))

empDir = [emp1, emp2]
print('\nPrint Employee Directory List')
print(empDir)

emp3 = ['Paul', 'BA', '2014']
emp4 = ['Bran', 'Manager', '2018']

print('\nAppending Dir list with a Emp list')
empDir.append(emp3)
print(empDir)

print('\nInserting Dir list with a Emp list')
empDir.insert(0, emp4)
print(empDir)

a = "abc"
