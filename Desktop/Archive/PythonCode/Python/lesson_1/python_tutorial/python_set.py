"""
Python Sets
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.
Set items are unordered, unchangeable, and do not allow duplicate values.
"""
# 1. Python - Access Set Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
# ex1:
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)
# ex2:
this_set = {"apple", "banana", "cherry"}
if "banana" in this_set:
    print("ok")
else:
    print("not found")
# 2. Python - Add Set Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
this_set = {"apple", "banana", "cherry"}
this_set.add("orange")
print(this_set)
# 3. Add Sets
# To add items from another set into the current set, use the update() method.
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)
print(this_set)
# 4. Python - Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
this_set = {"apple", "banana", "cherry"}
this_set.remove("cherry")
print(this_set)
this_set.discard("banana")
print(this_set)
# Remove the last item by using the pop() method:
this_set = {"apple", "banana", "cherry"}
this_set.pop()
print(this_set)
# The clear() method empties the set:
this_set = {"apple", "banana", "cherry"}
this_set.clear()
print(this_set)
# The del keyword will delete the set completely:
this_set = {"apple", "banana", "cherry"}
# del this_set
print(this_set)
# 5. Python - Loop Sets
this_set = {"apple", "banana", "cherry"}
for x in this_set:
  print(x)
