from config.db_settings import execute_query


def add_initiative(name, application_period, moderation_period, voting_period, allocated_funds):
    query = """INSERT INTO Initiatives 
                (name, application_period, moderation_period, voting_period, allocated_funds)
                VALUES (%s, %s, %s, %s, %s);
                """
    params = (name, application_period, moderation_period, voting_period, allocated_funds)
    execute_query(query=query, params=params)


def update_initiative(id, field, new_value):
    query = f"UPDATE Initiatives SET {field} = %s WHERE id = %s;"
    params = (new_value, id)
    execute_query(query=query, params=params)


def get_all_initiatives():
    query = "SELECT * FROM initiatives;"
    return execute_query(query=query, fetch='all')


def get_unstarted_initiatives():
    query = "SELECT * FROM Initiatives WHERE start_time IS NULL;"
    return execute_query(query=query, fetch='all')


def get_started_initiative():
    query = "SELECT * FROM Initiatives WHERE status = TRUE;"
    return execute_query(query=query, fetch='all')


def get_ended_initiatives():
    query = "SELECT * FROM Initiatives WHERE status = FALSE AND start_time IS NOT NULL;"
    return execute_query(query=query, fetch='all')


def get_initiative_by_id(id):
    query = "SELECT * FROM Initiatives WHERE id = %s;"
    params = (id,)
    return execute_query(query=query, params=params, fetch='one')
