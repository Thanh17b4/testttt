import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM customers")
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)
# note: neu dat ten file la select se xay ra loi vi trung ten voi func select trong package
# if want to fetch one record:
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM customers")
    my_result = my_cursor.fetchone()
    print(my_result)
