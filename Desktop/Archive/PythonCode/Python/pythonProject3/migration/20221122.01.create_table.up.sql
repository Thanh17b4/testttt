            CREATE TABLE jobs (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(255) NOT NULL,
                level VARCHAR(255) NOT NULL,
                salary VARCHAR(50) NOT NULL,
                CV_language VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                slug VARCHAR(255) NOT NULL,
                company_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                due_at  TIMESTAMP(6) NOT NULL
                );
            CREATE TABLE job_location (
                job_id INTEGER NOT NULL,
                location_name VARCHAR(30) NOT NULL,
                CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE
                );
            ALTER TABLE job_location
            ADD id SERIAL PRIMARY KEY NOT NULL;
            ALTER TABLE job_location
            ADD CONSTRAINT job_id_location_unique UNIQUE (job_id, location_name);

            ALTER TABLE job_location
            RENAME COLUMN location_name to location_id;

            CREATE TABLE job_category (
                id SERIAL PRIMARY KEY   NOT NULL,
                job_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT job_id_category_unique UNIQUE (job_id, category_id)
                );


            CREATE TABLE job_benefits (
                id SERIAL PRIMARY KEY NOT NULL,
                job_id INTEGER NOT NULL,
                benefit_id INTEGER NOT NULL,
                CONSTRAINT fk1 FOREIGN KEY  (job_id) REFERENCES jobs(id) ON UPDATE CASCADE ON DELETE CASCADE
                );

             ALTER TABLE job_benefits
            ADD CONSTRAINT fk_unique UNIQUE (job_id, benefit_id);




            ALTER TABLE job_benefits
            ADD id SERIAL PRIMARY KEY   NOT NULL;

            ALTER TABLE job_benefits
            ADD CONSTRAINT fk_unique UNIQUE (job_id, benefit_id);

            CREATE TABLE locations (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(30) NOT NULL ,
                slug VARCHAR(30) NOT NULL
                );


            ALTER TABLE locations
            ADD CONSTRAINT fk1_unique UNIQUE (name);

            CREATE TABLE categories (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL ,
                        slug VARCHAR(255) NOT NULL
                );

            CREATE TABLE benefits (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(30) NOT NULL ,
                        slug VARCHAR(30) NOT NULL
                );

            CREATE TABLE company (
                    id SERIAL PRIMARY KEY NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    address VARCHAR(255) NOT NULL,
                    website VARCHAR(255),
                    scale VARCHAR(50),
                    slug VARCHAR(255) NOT NULL,
                    contact VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );



