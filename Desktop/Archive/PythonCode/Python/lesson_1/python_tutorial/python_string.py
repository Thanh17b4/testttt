txt = "The best things in life are free!"
print("expensive" not in txt)

if "thanh" not in txt:
    print("thanh is not present in text")

b = " hello, world "
print(b[2:5])
# slice from start
print(b[:5])
# slice to the end
print(b[2:])
# negative index
print(b[-5:-2])

# Python - Modify Strings:
print(b.upper())  # upper case
print(b.lower())  # lower case
print(b.strip())  # strip case
print(b.replace("world", "Thanh"))  # replace string
print(b.split("r"))  # split string

# Python - string concatenation:
a = "hello"
b = "world"
c = a + b
d = a + " " + b  # insert whitespace into c
print(c)
print(d)

# Python - Format - Strings
age = 36
# msg = "My name is John, I am " + age -- could not combine string and integer but format method can do:
msg = "My name is John, I am {}"
print(msg.format(age))

quantity = 3
itemno = 567
price = 49.95
myOder = "I want {} pieaces of item {} for {} dollar"
print(myOder.format(quantity, itemno, price))

# Python - Escape Characters is used when want to insert character into string
txt1 = "We are the so-called \"Vikings\" from the north."
txt2 = 'It\'s alright'
txt3 = "Hello\nWorld!"
txt4 = "Hello\rWorld!"
txt5 = "Hello\tWorld!\tabc"  # will insert whiteTab between word
txt6 = "Hello \bWorld! \babc"  # will erase backspace character
txt7 = "Hello \fWorld! \fabc"
print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)
print(txt6)
print(txt7)

# ----------------------------------Python String capitalize() Method-------------------------------
# 1. Python String capitalize() Method:
# returns a string where the first character is upper case, and the rest is lower case.
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
# 2. Python String casefold() Method
# returns a string where all the characters are lower case.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
# 3. Python String casefold() Method
# will center align the string, using a specified character (space is default) as the fill character.
txt = "banana"
x = txt.center(10, "0")
print(x)
# 4. Python String count() Method
# returns the number of times a specified value appears in the string.
# syntax: string.count(value, start, end)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 7, 20)
print(x)
# 5. Python String encode() Method
# method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"
x = txt.encode()
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="strict"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
# 6. Python String find() Method
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
""" The find() method is almost the same as the index() method,
 the only difference is that the index() method raises an exception if the value is not found.
 (See example below) """
# Syntax: string.find(value, start, end)
txt = "Hello, wellcome my to world"
x = txt.find("w", 7, 23)
print(x)
"""example 2"""
# txt = "Hello, welcome to my world."
# print(txt.find("q"))
# print(txt.index("q"))

# 7. Python String format() Method
"""
formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}
"""
# Syntax: string.format(value1, value2...)
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))
print("For only {price:.2f} dollars!".format(price=49))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))