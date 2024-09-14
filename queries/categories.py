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


def get_categories_by_project_type(project_type_id):
    query = "SELECT * FROM Categories WHERE project_type_id = %s;"
    params = (project_type_id,)
    return execute_query(query=query, params=params, fetch='all')


def delete_category(id):
    query = f"DELETE FROM Categories WHERE id = %s;"
    params = (id,)
    execute_query(query=query, params=params)
