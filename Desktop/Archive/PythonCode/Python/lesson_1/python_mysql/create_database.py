import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345"
)
    my_cursor = mydb.cursor()
    # my_cursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("SHOW DATABASES")
    for x in my_cursor:
        print(x)

# Try connecting to the database "mydatabase":
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="mydatabase"
    )
