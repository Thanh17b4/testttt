"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones: (), [], {}"""

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 10
b = 9
if a > b:
    print("a is bigger than b")
else:
    print("a is smaller than b")

print(bool("hello"))
print(bool(15))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
"""
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class 
with a __len__ function that returns 0 or False:
"""

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

"Functions can Return a Boolean"
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
