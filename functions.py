# functions in python

def my_function():
    print('hello i am a function')

my_function()   # function call

#-----------------------------------------
#passing arguments

def greet(name):
    print("hello " + name)

greet('ram')
greet('sita')

#------------------------------------------
#default parameter

def greets(name = "computer"):
    print("hello " + name)

greets()
greets("mike")