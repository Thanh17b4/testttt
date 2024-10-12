
import pymongo
from general_func.model import myfunc
from general_func.model import myfunc
if __name__ == '__main__':
    x = myfunc().find_one()
    print(x)
# if want to find all records:
if __name__ == '__main__':
    x = myfunc().find()
    for y in x:
        print(y)
# Return Only Some Fields: Return only the names and addresses, not the _ids:
if __name__ == '__main__':
    x = myfunc().find({}, {'_id': 0, 'name': 1, 'address': 1})
    for y in x:
        print(y)
"""
You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
If you specify a field with the value 0, all other fields get the value 1, and vice versa:
"""
# Return only the names and id, not the "address" field:
if __name__ == '__main__':
    x = myfunc().find({}, {"address": 0})
    for y in x:
        print(y.values())






