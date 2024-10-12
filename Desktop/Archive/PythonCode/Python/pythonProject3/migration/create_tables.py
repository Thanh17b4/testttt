import psycopg2
import config


def create_tables():
    # create tables in the PostgresSQL database
    commands = (
        """
            CREATE TABLE jobs (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(255) NOT NULL, 
                level VARCHAR(255) NOT NULL,
                CV_language VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                slug VARCHAR(255) NOT NULL,
                company_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                due_at  TIMESTAMP(6) NOT NULL
            )
            """,
        """
                CREATE TABLE job_location (
                        job_id INTEGER NOT NULL,
                        location_name VARCHAR(30) NOT NULL,
                        CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE
                )
                """,
        """
                CREATE TABLE job_category (
                        job_id INTEGER NOT NULL,
                        category_id VARCHAR(255) NOT NULL,
                        CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE
                )
                """,
        """
                CREATE TABLE job_benefits (
                        job_id INTEGER NOT NULL,
                        benefit_id VARCHAR(30) NOT NULL,
                        CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE
                )
                """,

        """
        CREATE TABLE locations (
                name VARCHAR(30) PRIMARY KEY,
                slug VARCHAR(30) NOT NULL
        )
        """,

        """
                CREATE TABLE categories (
                        id SERIAL PRIMARY KEY,
                        c_name VARCHAR(255) NOT NULL ,
                        slug VARCHAR(255) NOT NULL
                )
                """,

        """
                CREATE TABLE benefits (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(30) NOT NULL ,
                        slug VARCHAR(30) NOT NULL
                )
                """,

        """ CREATE TABLE company (
                    id SERIAL PRIMARY KEY NOT NULL,
                    name VARCHAR(255) NOT NULL, 
                    address VARCHAR(255) NOT NULL,
                    website VARCHAR(255),
                    scale VARCHAR(50),
                    slug VARCHAR(255) NOT NULL,
                    contact VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP
                    )
                """
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
    create_tables()
