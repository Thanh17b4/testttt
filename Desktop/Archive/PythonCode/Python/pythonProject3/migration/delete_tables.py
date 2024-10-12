import psycopg2


def delete_tables():
    commands = (
        "drop table benefits",
        "drop table categories",
        "drop table company",
        "drop table locations",
        "drop table job_benefits",
        "drop table job_category",
        "drop table job_location",
        "drop table jobs"
    )
    try:
        # connect to the PostgresSQL server
        conn = psycopg2.connect(
            host="localhost",
            database="test_db",
            user="thanhpv",
            password="22121992")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgresSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    delete_tables()