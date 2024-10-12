from config.db import db

if __name__ == '__main__':
    list1 = [
        {"name": "Peter", "email": "abc@gmail.com", "role": "admin", "verified": "yes", "password": "22121992Th"},
        {"name": "Peter", "email": "cde@gmail.com", "role": "manager", "verified": "yes", "password": "22121992Th"},
        {"name": "Peter", "email": "edf@gmail.com", "role": "staff", "verified": "yes", "password": "22121992Th"},
        {"name": "Peter", "email": "ghk@gmail.com", "role": "user", "verified": "yes", "password": "22121992Th"},
    ]
    y = db()["users"].insert_many(list1)
    print(y.inserted_ids)
