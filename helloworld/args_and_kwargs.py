# https://www.geeksforgeeks.org/args-kwargs-python
# Special Symbols Used for passing arguments:-

# 1.)*args (Non-Keyword Arguments)

# 2.)**kwargs (Keyword Arguments)

# Python program to illustrate
# *args for variable number of arguments
print("-------Example 1-------")


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *args with first extra argument
print("-------Example 2-------")


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kargs for variable number of keyword arguments
print("-------Example 3-------")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# Using *args and **kwargs to call a function
print("-------Example 4-------")


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# kwargs = {"arg4": "Geeks", "arg2": "for", "arg3": "Geeks"} #ERROR
myFun(**kwargs)

# Using *args and **kwargs in same line to call a function
print("-------Example 5-------")


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
