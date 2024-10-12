"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
lists are defined as objects with the data type 'list': <class 'list'>
"""
thisList = ["apple", "banana", "cherry"]
print(thisList)
print(len(thisList))
print(type(thisList))
# Using the list() constructor to make a List:
thisList = list(("apple", "banana", "cherry"))
print(thisList)

"""
Access Items: List items are indexed and you can access them by referring to the index number
Negative indexing means start from the end
"""
print(thisList[0])
print(thisList[-1])
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])  # The search will start at index 2 (included) and end at index 5 (not included).
print(thisList[-4:-1])  # The search will start at index -4 (included) and end at index -1 (not included).
if "apple" in thisList:  # To determine if a specified item is present in a list use the in keyword:
    print("yes, apple in fruit list")

"""
Python - Change List Items:
To change the value of a specific item, refer to the index number
"""
thisList[1] = "blackcurrant"
print(thisList)
# If you insert more items than you replace, the new items will be inserted where you specified
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)

"""Insert Items: we can insert new item by use insert() method"""
thisList.insert(1, "banana")
print(thisList)

"""Python - Add List Items"""
# To add an item to the end of the list, use the append() method:
thisList = ["banana", "apple", "cherry"]
thisList.append("orange")
print(thisList)
# To insert a list item at a specified index, use the insert() method.
# Extend List: To append elements from another list to the current list, use the extend() method.
thisList = ["banana", "apple", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

tuple = ("mango", "pineapple", "papaya")
thisList.extend(tuple)  # you can add any iterable object (tuples, sets, dictionaries etc.) by extend() method
print(thisList)

"""Python - Remove List Items"""
# Remove Specified Item: The remove() method removes the specified item.
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)
# Remove Specified Index: The pop() method removes the specified index.
thisList.pop(1)
print(thisList)
thisList = ["apple", "banana", "cherry"]
thisList.pop()  # If you do not specify the index, the pop() method removes the last item
print(thisList)
# The del keyword also removes the specified index:
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)
# Clear the List by The clear() method empties the list. The list still remains, but it has no content.
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

"""Python - Loop Lists"""
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)
# Use the range() and len() functions to create a suitable iterable.
for i in range(len(thisList)):
    print(thisList[i])
# using a while loop.
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1
# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

"""List Comprehension"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)
# short syntax: newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""sort list
List objects have a sort() method that will sort the list alphanumerically, ascending, by default
To sort descending, use the keyword argument reverse = True
By default the sort() method: resulting in all capital letters being sorted before lower case letters
"""
# ex1:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort()
print(thisList)
# ex2:
thisList = [10, 20, 30, 40, 50]
thisList.sort(reverse=True)  # = thisList.reverse()
print(thisList)
# ex3:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort(key=str.lower)
print(thisList)

"""Python - Copy Lists
You cannot copy a list simply by typing list2 = list1
There are ways to make a copy, one way is to use the built-in List method copy()
Another way to make a copy is to use the built-in method list().
"""
# ex1:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
myList = thisList.copy()
print(myList)
# ex2:
thisList = ["banana", "Orange", "Kiwi", "cherry"]
myList = list(thisList)
print(myList)

"""
Python - Join Lists
"""
# by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# by using extend() method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

"""
Python List count() Method
returns the number of elements with the specified value.
"""
# ex1:
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry")
print(x)
