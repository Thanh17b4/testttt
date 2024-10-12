"""
Python Tuples:
Tuples are used to store multiple items in a single variable.
Tuples are written with round brackets
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Type: <class 'tuple'>
"""
# ex1:
myTuple = ("apple", "banana", "cherry", "banana")
print(myTuple)
print(type(myTuple))
print(len(myTuple))
# ex2:
this_tuple = tuple(("apple", "banana", "cherry"))
print(this_tuple)
"1. Python - Access Tuple Items"
# You can access tuple items by referring to the index number, inside square brackets:
# ex1:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[-1])
"2. Python - Update Tuples"
# you cannot change, add, or remove items once the tuple is created. but there are some workarounds.
# 2.1 Change Tuple Values by convert the tuple into a list, change the list, and convert the list back into a tuple.
# ex1:
my_tuple = ("apple", "banana", "cherry", "banana")
x = list(my_tuple)
x[1] = "kiwi"
my_tuple = tuple(x)
print(my_tuple)
# 2.2 add tuple to a tuple
# You are allowed to add tuples to tuples, so if you want to add one item, (or many),
# create a new tuple with the item(s), and add it to the existing tuple
# When creating a tuple with only one item, remember to include a comma after the item
# ex1:
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y
print(this_tuple)
# 2.3 Remove Items
# as same as change tuple
this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)
print(this_tuple)
# when delete total tuple:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
"3. Python - Unpack Tuples"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# Note: The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


