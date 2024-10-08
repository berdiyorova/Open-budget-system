from config.db_settings import execute_query


def create_appeal_type():
    return """
        DO $$  
            BEGIN  
                IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'appeal_status') THEN  
                    CREATE TYPE appeal_status AS ENUM ('in_process', 'accepted', 'rejected', 'winner');  
                END IF;  
            END $$;
        """

def create_regions_table():
    return """
        CREATE TABLE IF NOT EXISTS Regions (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64)
        );
        """

def create_districts_table():
    return """
        CREATE TABLE IF NOT EXISTS districts (
        id SERIAL PRIMARY KEY,
        region_id INT,
        name VARCHAR(64),
        FOREIGN KEY (region_id) REFERENCES Regions(id)
        );
        """

def create_users_table():
    return """
        CREATE TABLE IF NOT EXISTS Users (  
        uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,  
        first_name VARCHAR(32) NOT NULL,  
        last_name VARCHAR(32) NOT NULL,
        birth_date DATE NOT NULL,
        profession VARCHAR(64) NOT NULL,
        gender VARCHAR(8) NOT NULL,
        is_login BOOLEAN DEFAULT FALSE,
        phone VARCHAR(16) NOT NULL UNIQUE,
        email VARCHAR(32) NOT NULL UNIQUE, 
        region_id INT,
        district_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        FOREIGN KEY (region_id) REFERENCES Regions(id),
        FOREIGN KEY (district_id) REFERENCES Districts(id)
    );  
        """

def create_initiatives_table():
    return """
        CREATE TABLE IF NOT EXISTS Initiatives (  
        id SERIAL PRIMARY KEY,  
        name TEXT NOT NULL,
        start_time DATE,
        application_period INTERVAL,
        moderation_period INTERVAL,
        voting_period INTERVAL,
        status BOOLEAN DEFAULT FALSE,
        allocated_funds NUMERIC(15, 0),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
    );  
        """


def create_project_types_table():
    return """
        CREATE TABLE IF NOT EXISTS Project_types (
        id SERIAL PRIMARY KEY,
        name VARCHAR(256)
        );
        """

def create_categories_table():
    return """
        CREATE TABLE IF NOT EXISTS Categories (
        id SERIAL PRIMARY KEY,
        project_type_id INT,
        name VARCHAR(256),
        FOREIGN KEY (project_type_id) REFERENCES Project_types(id)
        );
        """

def create_appeals_table():
    return """
        CREATE TABLE IF NOT EXISTS Appeals (
        id SERIAL PRIMARY KEY,
        user_id UUID NOT NULL,
        initiative_id INT NOT NULL,
        category_id INT NOT NULL,
        region_id INT NOT NULL,
        district_id INT NOT NULL,
        title VARCHAR(128),
        status APPEAL_STATUS DEFAULT 'in_process',
        funds_offered NUMERIC(12, 2),
        funds_approved NUMERIC(12, 2),
        votes INT DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users(uuid),
        FOREIGN KEY (initiative_id) REFERENCES Initiatives(id),
        FOREIGN KEY (category_id) REFERENCES Categories(id),
        FOREIGN KEY (region_id) REFERENCES Regions(id),
        FOREIGN KEY (district_id) REFERENCES Districts(id)
        )
        """

def create_votes_table():
    return """
        CREATE TABLE IF NOT EXISTS Votes (
        initiative_id INT,
        appeal_id INT,
        email VARCHAR(32) NOT NULL,
        FOREIGN KEY (initiative_id) REFERENCES Initiatives(id),
        FOREIGN KEY (appeal_id) REFERENCES Appeals(id),
        PRIMARY KEY (initiative_id, appeal_id, email)
        );
        """


def create_all_tables():
    query = create_appeal_type()
    execute_query(query)

    query = create_regions_table()
    execute_query(query)

    query = create_districts_table()
    execute_query(query)

    query = create_users_table()
    execute_query(query)

    query = create_initiatives_table()
    execute_query(query)

    query = create_project_types_table()
    execute_query(query)

    query = create_categories_table()
    execute_query(query)

    query = create_appeals_table()
    execute_query(query)

    query = create_votes_table()
    execute_query(query)
