import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    # my_cursor.execute("""CREATE TABLE users(
    #                                     id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #                                     name      varchar(255) NOT NULL,
    #                                     email     varchar(255) NOT NULL,
    #                                     protected tinyint(1) NOT NULL DEFAULT 0,
    #                                     banned    tinyint(1) NOT NULL DEFAULT 0,
    #                                     activated tinyint(1) NOT NULL DEFAULT 0,
    #                                     address   varchar(255) NOT NULL,
    #                                     password  varchar(255) NOT NULL,
    #                                     username  varchar(255) NOT NULL,
    #                                     CONSTRAINT users_email_unique UNIQUE (email)
    #                                     )"""
    #                   )

# show tables
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("show tables")
    for x in my_cursor:
        print(x)
# add foreign key
# if __name__ == '__main__':
#     mydb = mysql.connector.connect(
#         host="localhost",
#         username="root",
#         password="12345",
#         database="mydatabase"
#     )
#     my_cursor = mydb.cursor()
#     my_cursor.execute("ALTER TABLE users ADD CONSTRAINT users_username_unique UNIQUE (username) ")
# create customers table
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="mydatabase"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE customes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
