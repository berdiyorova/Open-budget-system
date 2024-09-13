from config.db_settings import execute_query


def add_user(first_name, last_name, birth_date, profession, phone, email, gender, region_id, district_id):
    query = """INSERT INTO Users 
            (first_name, last_name, birth_date, profession, phone, email, gender, region_id, district_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
    params = (first_name, last_name, birth_date, profession, phone, email, gender, region_id, district_id)
    execute_query(query=query, params=params)


def get_user(phone):
    query = "SELECT * FROM Users u WHERE u.phone = %s;"
    params = (phone,)
    return execute_query(query, params, 'one')


def get_user_by_id(uuid):
    query = "SELECT * FROM Users u WHERE u.uuid = %s;"
    params = (uuid,)
    return execute_query(query=query, params=params, fetch='one')


def get_all_users():
    query = "SELECT first_name, last_name, phone FROM Users;"
    return execute_query(query=query, fetch='all')


def update_user(id, field, new_value):
    query = f"UPDATE Users SET {field} = %s WHERE id = %s);"
    params = (new_value, id)
    execute_query(query=query, params=params)
