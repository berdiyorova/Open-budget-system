from config.db_settings import execute_query


def add_category(name):
    query = """INSERT INTO Project_types 
                (name)
                VALUES (%s);
                """
    params = (name,)
    execute_query(query=query, params=params)


def update_pr_type(id, field, new_value):
    query = f"UPDATE Project_types SET {field} = %s WHERE id = %s;"
    params = (new_value, id)
    execute_query(query=query, params=params)


def get_all_project_types():
    query = "SELECT name FROM project_types;"
    return execute_query(query=query, fetch='all')


def delete_pr_type(id):
    query = f"DELETE FROM Project_types WHERE id = %s;"
    params = (id,)
    execute_query(query=query, params=params)
