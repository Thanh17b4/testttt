"Python Functions"
# 1. Creating a Function by using the "def" keyword:
# To call a function, use the function name followed by parenthesis:
if __name__ == '__main__':
    def my_function():
        print("hello from a function")
    my_function()
# 2. Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
if __name__ == '__main__':
    def my_function(f_name, l_name):
        print(f_name + " " + l_name + " " + "Pham")
    my_function("Thanh", "Van")
    my_function("Chi", "Van")
# 2.1 Arbitrary Arguments, *args
if __name__ == '__main__':
    def my_function(*kid):
        print("the youngest kid is: " + kid[2])
    my_function("Tom", "Jery", "Halland")
# 2.2 Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
if __name__ == '__main__':
    def my_function(child1, child2, child3):
        print("the youngest kid is: " + child3)
    my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# 2.3 Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
if __name__ == '__main__':
    def my_function(**kid):
        print("his last name is: " + kid["l_name"])
    my_function(f_name = "Tobias", l_name = "Refsnes")
# ex2: Passing a List as an Argument
if __name__ == '__main__':
    def my_function(food):
        for x in food:
            print(x)
    fruits = ["apple", "banana", "cherry"]
    my_function(fruits)
# 2.4 Recursion
if __name__ == '__main__':
    def my_recursion(k):
        if (k > 0):
            result = k + my_recursion(k-1)
            print(result)
        else:
            result = 0
        return result
    print("\nRecursion Example Results")
    my_recursion(6)