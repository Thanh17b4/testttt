"""
Python Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if __name__ == '__main__':
    print(this_dict)
    print(this_dict["model"])
#  1. Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets or method get
if __name__ == '__main__':
    this_dict.get("model")
if __name__ == '__main__':
    x = this_dict.keys()
    print(x)
if __name__ == '__main__':
    x = this_dict.values()
    print(x)
if __name__ == '__main__':
    x = this_dict.items()
    print(x)
if __name__ == '__main__':
    if "model" in this_dict:
        print("ok")
    else:
        print("Not haven")

# 2. Python - Change Dictionary Items
if __name__ == '__main__':
    this_dict["year"] = 2018
    print(this_dict)
if __name__ == '__main__':
    this_dict.update({"year": 2020})
    print(this_dict)
# 3. Python - Add Dictionary Items
# 3.1 Adding an item to the dictionary is done by using a new index key and assigning a value to it:
if __name__ == '__main__':
    this_dict["color"] = "red"
    print(this_dict)
# 3.2 Adding an item to the dictionary is done by using update() method
if __name__ == '__main__':
    this_dict.update({"color": "red"})
    print(this_dict)
# 4. Python - Remove Dictionary Items
# 4.1 The pop() method removes the item with the specified key name
if __name__ == '__main__':
    this_dict.pop("model")
    print(this_dict)
# 4.2 The popitem() method removes the last inserted item
if __name__ == '__main__':
    this_dict.popitem()
    print(this_dict)
