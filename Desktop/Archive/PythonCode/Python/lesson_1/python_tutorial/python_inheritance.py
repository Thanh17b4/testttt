"""
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""
# ex1:
if __name__ == '__main__':
    class Person:
        def __init__(self, f_name, l_name):
            self.first_name = f_name
            self.last_name = l_name

        def printname(self):
            print(self.first_name, self.last_name)


    x = Person("John", "Doe")
    x.printname()
# ex2:
if __name__ == '__main__':
    class Person:
        def __init__(self, fname, lname):
            self.first_name = fname
            self.last_name = lname

        def print_name(self):
            print(self.first_name, self.last_name)

    class Student(Person):
        def __init__(self, fname, lname):
            Person.__init__(self, fname, lname)

    x = Student("Mike", "Olsen")
    x.print_name()

# Python also has a super() function that will make the child class inherit
# all the methods and properties from its parent:
if __name__ == '__main__':
    class Person:
        def __init__(self, fname, lname):
            self.first_name = fname
            self.last_name = lname

        def print_name(self):
            print(self.first_name, self.last_name)

    class Student(Person):
        def __init__(self, fname, lname):
            super().__init__(fname, lname)
            self.graduationyear = 2019

        def Wellcome(self):
            print("wellcome", self.first_name, self.last_name, "to the class of", self.graduationyear)

    x = Student("Mike", "Olsen")
    x.Wellcome()




