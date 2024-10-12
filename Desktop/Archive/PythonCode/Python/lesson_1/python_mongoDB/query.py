from general_func.model import myfunc
# to find the documents where the "address" field starts with the letter "S" or higher (alphabetically)
if __name__ == '__main__':
    condition = {'_id': 5}
    # condition = { "address": {"$gt": "S"} }
    x = myfunc().find(condition)
    for y in x:
        print(y)
# Find documents where the address starts with the letter "S":
if __name__ == '__main__':
    condition = { "address": {"$regex": "^S"} }
    x = myfunc().find(condition)
    for y in x:
        print(y)
# sort() method:
# sort("name", 1)  ascending: default
# sort("name", -1) descending
if __name__ == '__main__':
    x = myfunc().find().sort("name", -1)
    for y in x:
        print(y)
if __name__ == '__main__':
    # condition = {'_id': 5}
    x = myfunc().find()
    for y in x:
        print([y.values()])