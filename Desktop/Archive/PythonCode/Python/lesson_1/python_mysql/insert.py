import datetime
from slugify import slugify
import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    job = {'name': 'Chuyên Gia Ngân Sách Tài Chính và Kế Hoạch', 'company_id': 1, 'level': 'Nhan vien',
           'type': 'toan thoi gian', 'cv_language': 'tieng viet',
           'due_at': datetime.datetime(2022, 12, 13, 9, 33, 25, 224126)}
    print(job["name"])
    slug = slugify(job["name"])
    print(slug)
    due_at = datetime.datetime.now() + datetime.timedelta(days=20)
    sql = "INSERT INTO jobs (name, cv_language, type, slug, company_id, level, due_at) VALUE (%s, %s, %s, %s, %s, %s, %s)"
    val = (job["name"], job["cv_language"], job["type"], slug, job["company_id"], job["level"], due_at)
    new_job = my_cursor.execute(sql, val)
    # my_cursor.execute("INSERT INTO customers (name, address) VALUE ('Thanh', 1)")
    my_cursor.execute(sql, val)
    mydb.commit()
    print(my_cursor.rowcount, "record inserted.")
# Important!: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

# Insert Multiple Rows use executemany() method
# if __name__ == '__main__':
#     mydb = mysql.connector.connect(
#         host="localhost",
#         username="root",
#         password="12345",
#         database="mydatabase"
#     )
#     my_cursor = mydb.cursor()
#     sql = "INSERT INTO customers (name, address) VALUE (%s, %s)"
#     val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#     my_cursor.executemany(sql, val)
#     mydb.commit()
#     print(my_cursor.rowcount, "record inserted.", my_cursor.lastrowid)
