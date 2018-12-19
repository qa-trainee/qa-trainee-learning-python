# ATBS_S1_L7.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 1, Lecture 7

# for loop

# for i in range(5)
# range (5) stops at 4
# you can give multiple arguement to range like range(5, 10)
# this will continue from 5 till 9

import datetime

print('This program prints a sum of all integers from ie 1+2+3 ...+number')
print('enter an integer number')
number = int(input())

start = str(datetime.datetime.now().time())
print('Code started at ' + start)

sum = 0
for i in range(1, number+1):
    sum = sum + i
print('Total is ' + str(sum))
end = str(datetime.datetime.now().time())

print('Code ended at ' + end)
FMT = '%H:%M:%S.%f'
tdelta = datetime.datetime.strptime(end, FMT) - \
    datetime.datetime.strptime(start, FMT)
print('Code took this much time to execute: ' + str(tdelta))
