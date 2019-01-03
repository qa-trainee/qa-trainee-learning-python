# ATBS_S6_L13.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 13

# List data datatype
# spam = ['cat','bat','rat']
# list can have other list as its individual values
# list index. spam[0] gives cat, spam[1] gives bat, spam[2] gives rat.
# spam[-1] gives the last value in list, span [-2] gives second last
# if index is wrong then IndexError list index out of range is raised
# slice format is used to get a part of lists
# spam[1:3] will give spam list's index 1 to 3 in a list format
# spam [:2] will slice from 0 till 2
# spam [2:] will slice from 2 till end
# del spam[2] can be used to delete something from list
# list function can convert parameters and retunr lists
# in operator can give true and false depending on if value is present in lists
# 'cat' in spam == True

spam = ['cat', 'bat', 'rat']

print('For loop with poistive index lists')
for i in range(0, 10):
    try:
        print(str(i) + ': ' + spam[i])
    except IndexError as e:
        print(str(i) + ': ' + str(e))
        continue

print('While loop with negative index lists')
i = -5
while i < 5:
    try:
        i = i + 1
        print(str(i) + ': ' + spam[i])
    except IndexError as e:
        print(str(i) + ': ' + str(e))
        continue
