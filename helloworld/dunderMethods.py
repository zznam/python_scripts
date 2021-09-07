
# https://www.geeksforgeeks.org/__new__-in-python/

# Double Underscores
class class_name:
    # _new__ method will be called when an object is created
    def __new__(cls, *args, **kwargs):
        # statements
        # .
        # .
        return super(class_name, cls).__new__(cls, *args, **kwargs)
    #  __init__ method will be called to initialize the object
    def __init__(self) -> None:
        pass



# Python program to 
# demonstrate __new__

print("-------Example 1-------")
# don't forget the object specified as base
class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
  
A()


print("-------Example 2-------")
  
class B(object):
    def __new__(cls):
        print("Creating instance")
  
    # It is not called
    def __init__(self):
        print("Init is called")
  
print(B())


print("-------Example 3-------")

class C(object):
    # new method returning a string
    def __new__(cls):
        print("Creating instance")
        return "GeeksforGeeks"
  
class D(object):
    # init method returning a string
    def __init__(self):
        print("Initializing instance")
        # return "GeeksforGeeks" #__init__() should return None, not 'str'
  
print(C())
print(D())


print("-------Example 4-------")

#  class whose object
# is returned
class GeeksforGeeks(object):
    def __str__(self):
        return "GeeksforGeeks"
          
# class returning object
# of different class
class Geek(object):
    def __new__(cls):
        return GeeksforGeeks()
          
    def __init__(self):
        print("Inside init")
          
print(Geek())