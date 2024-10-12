from general_func.model import myfunc
if __name__ == '__main__':
    condition = {"address": "Valley 345"}
    new_value = {"$set": { "address": "Canyon 123" }}
    myfunc().update_one(condition, new_value)
    for y in myfunc().find():
        print(y)
# update many record
if __name__ == '__main__':
    condition = {"_id": {'$gte': 10}}
    new_value = {"$set": {"address": "Canyon 123" }}
    myfunc().update_many(condition,  new_value)
    for y in myfunc().find():
        print(y)