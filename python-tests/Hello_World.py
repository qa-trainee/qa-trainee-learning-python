# this is a comment
# this is a comment
# block ok please
# bye

# print function accepts strings to print on console
print("Hello World!")
print("Whats your name?")
# input function accepts strings and puts them on myName variable
myName = input()
# print with a variable which is a string
print("Nice to meet you, " + myName)
# using str to convert the integer to str, similarly int and float is there
print("Length of your name is " + str(len(myName)) + " charecters")
# input with a text message and variable assignment in the same line
myAge = input("What is your age? : ")
# print with an escape charecter \ to escape single quotes ' and display
# them as it is
print(myName + "\'s age is \'" + myAge + "\' years.")
yearsTill60 = 60 - int(myAge)
print("You will be 60 years old in just " + str(yearsTill60) + " more years!")
