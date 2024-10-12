import pymongo
def myfunc():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    DB = client["mongoDB"]
    collection = DB["customers"]
    return collection
    # mydict = {"_id": 17, "name": "John", "address": "Highway 37"}
    # x = collection.insert_one(mydict)
    # list_of_db = client.list_database_names()
    #
    # print("list DB:", list_of_db),
    # print("inserted DB:", list_of_db[-1])
    # print("collection:", collection.name)
    # print("inserted record id:", x.inserted_id)
    # if "mongoDB" in list_of_db:
    #     print("ok !!")
    # else:
    #     print("no have")
def testfunc(x):
    print(x + 1)