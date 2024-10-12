from general_func.model import myfunc
if __name__ == '__main__':
    condition = {"address": "Highway 37"}
    myfunc().delete_one(condition)
    x = myfunc().find()
    for y in x:
        print(y)

# delete all account:
if __name__ == '__main__':
    x = myfunc().delete_many({})
    print(x.deleted_count, "id have been deleted")

# drop collection:
if __name__ == '__main__':
    myfunc().drop()
    print(myfunc().name)