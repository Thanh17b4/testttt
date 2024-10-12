"""
Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating
a database, you should complete the next two chapters (create collection and create document)
before you check if the database exists!
"""
import pymongo
if __name__ == '__main__':
            client = pymongo3.MongoClient("mongodb://bitkub:bitkub@localhost:27017/")
            db = client["mongoDB"]
            collection = db["users"]
            mydict = {"name": "Thanh", "okta_id": "ssefsdsfdfs"}
            x = collection.insert_one(mydict)
            list_of_db = client.list_database_names()

            print("list db:", list_of_db),
            print("inserted db:", list_of_db[-1])
            print("collection:", collection.name)
            # print("inserted record id:", x.inserted_id)
            if "mongoDB" in list_of_db:
                print("ok !!")
            else:
                print("no have")
# insert many records:
if __name__ == '__main__':
            list1 = [
                {"_id": 1, "name": "John", "address": "Highway 37"},
                {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
                {"_id": 3, "name": "Amy", "address": "Apple st 652"},
                {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
                {"_id": 5, "name": "Michael", "address": "Valley 345"},
                {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
                {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
                {"_id": 8, "name": "Richard", "address": "Sky st 331"},
                {"_id": 9, "name": "Susan", "address": "One way 98"},
                {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
                {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
                {"_id": 12, "name": "William", "address": "Central st 954"},
                {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
                {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
            ]
            y = collection.insert_many(list1)
            print(y.inserted_ids)


