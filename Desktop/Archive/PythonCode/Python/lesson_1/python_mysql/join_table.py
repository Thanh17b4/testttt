import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="12345",
        database="token"
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("""SELECT u.id, u.name as user, uo.otp
                        FROM users u
                        INNER JOIN users_otp uo ON u.id = uo.user_id 
                        ORDER BY uo.created_at DESC limit 1
                        """)
    my_result = my_cursor.fetchall()
    for x in my_result:
        print(x)