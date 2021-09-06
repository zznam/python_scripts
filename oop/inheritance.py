class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    #add properties etc.
#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()