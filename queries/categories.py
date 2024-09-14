from config.db_settings import execute_query


def add_category(project_type_id, name):
    query = """INSERT INTO Categories 
                (project_type_id, name)
                VALUES (%s, %s);
                """
    params = (project_type_id, name)
    execute_query(query=query, params=params)


def update_category(id, field, new_value):
    query = f"UPDATE Categories SET {field} = %s WHERE id = %s;"
    params = (new_value, id)
    execute_query(query=query, params=params)


def get_all_categories():
    query = "SELECT * FROM Categories;"
    return execute_query(query=query, fetch='all')


def delete_category(id):
    query = f"DELETE FROM Categories WHERE id = %s;"
    params = (id,)
    execute_query(query=query, params=params)
