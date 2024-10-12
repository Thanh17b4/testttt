if __name__ == '__main__':
    class My_class:
        x = 0


    p1 = My_class()
    print(p1.x)

if __name__ == '__main__':
    class Person:
        def __init__(info, name, age):
            info.name = name
            info.age = age


    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# 2. The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned
if __name__ == '__main__':
    class Person:
        def __init__(info, name, age):
            info.name = name
            info.age = age


    p1 = Person("John", 36)
    print(p1)
# The string representation of an object WITH the __str__() function:
if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name}({self.age})"
    p1 = Person("John", 36)
    print(p1)
# Insert a function that prints a greeting, and execute it on the p1 object:
if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def my_func(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    p1.my_func()
    p1.age = 40
    print(p1.age)
# Delete Object Properties
if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def my_func(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    del p1.age
    print(p1.age)


