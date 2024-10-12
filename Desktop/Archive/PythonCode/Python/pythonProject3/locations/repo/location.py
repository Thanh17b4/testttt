
from locations.db import mydb
from locations.schemas import Location


def create_location_repo(req: Location):
    location = req.location_to_dict()
    with mydb:
        my_cursor = mydb.cursor()
        sql = "INSERT INTO locations (name, slug) VALUES (%s, %s)"
        val = (location["name"], location["slug"])
        my_cursor.execute(sql, val)
        mydb.commit()
    return f"{my_cursor.rowcount} location has been inserted successfully"
