"Python Lambda"
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda <arguments> : <expression>
# ex1:
if __name__ == '__main__':
    x = lambda a, b: a * b
    print(x(10, 10))
# ex2:
if __name__ == '__main__':
    def my_func(n):
        return lambda a: a * n
    double = my_func(2)
    tripler = my_func(3)
    print(double(10))
    print(tripler(11))


