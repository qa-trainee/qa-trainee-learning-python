# ATBS_S7_L17.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 6, Lecture 17

# Dictionary data type

# Dictionary data type has list of key and value pairsself
# it is not in a sequence, sequence does not matter
# it is created using curly bracket
# you can use 'keyname' in dictname to evaluate True or False
# dictname.keys(), values(), items() return list like valuesself.
# dictname.get('keyname', default value) returns key value if it exists
# or default value


# Function that returns number of occurances of a variable in a sentence

import pprint
stmt = 'my name is mandar rane'
print(stmt)

count = {}

for i in stmt:
    # checks if key exists in dir, if not then add with default value
    count.setdefault(i, 0)
    # Increments the count, modifying value of a key in directory
    count[i] = count[i] + 1

# printing dictionary
print(count)

# printing dir key values on different lines
# count.items returns key value pairs
for a, b in count.items():
    print(a, b)

print(list(count.keys()))
print(list(count.values()))
print(list(count.items()))

# printing dictionary in better pformat
pprint.pprint(count)
# to save pprint in a string variable
# count = pprint.pformat(count)
