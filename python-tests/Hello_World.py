# this is a comment
# Collections has namedtuple which is used in NameAndAge() to demonstrate
# a function returning mutiple values
import collections


def sum(bacon):
    bacon = bacon * 3
    print(bacon)


def HelloWorld():
    # print function accepts strings to print on console
    print("Hello World!")
    print("Exiting HelloWorld Function")
    print("")


def NameAndAge():
    print("")
    print("Hello, you are now in NameAndAge function")
    print("I will note down your name and age and return it to main function")
    print("")
    print("Whats your name?")
    # input function accepts strings and puts them on myName variable
    myName = input()
    # print with a variable which is a string
    print("")
    print("Nice to meet you, " + myName)
    # using str to convert the integer to str, similarly int and float can be
    # used for those datatypes
    print("Did you know that the length of your name is " +
          str(len(myName)) + " charecters")
    # input with a text message and variable assignment in the same line
    print("")
    myAge = input("What is your age? : ")
    # print with an escape charecter \ to escape single quotes ' and display
    # them as it is
    print(myName + "\'s age is \'" + myAge + "\' years.")
    yearsTill60 = 60 - int(myAge)
    print(myName + " will be 60 years old in just " +
          str(yearsTill60) + " more years!")
    # using namedtules to store and return multiple values
    NameAgeTuple = collections.namedtuple('NameAgeTuple', ['Name', 'Age'])
    p = NameAgeTuple(myName, myAge)
    print("")
    print("Exiting NameAndAge function")
    print("")
    return p


# HelloWorld()
# UsersNameAndAge = NameAndAge()
# print(UsersNameAndAge.Name)
# print(UsersNameAndAge.Age)
sum("spam")
