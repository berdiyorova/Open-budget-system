from config.db_settings import execute_query


def add_appeal(user_id, initiative_id, category_id, region_id, district_id, title, funds_offered):
    query = """INSERT INTO Appeals 
                (user_id, initiative_id, category_id, region_id, district_id, title, funds_offered)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
    params = (user_id, initiative_id, category_id, region_id, district_id, title, funds_offered)
    execute_query(query=query, params=params)


def get_all_appeals():
    query = "SELECT * FROM Appeals;"
    return execute_query(query=query, fetch='all')


def get_all_appeals_in_initiative(initiative_id):
    query = "SELECT * FROM Appeals WHERE initiative_id = %s;"
    params = (initiative_id,)
    return execute_query(query=query, params=params, fetch='all')


def get_new_appeals():
    query = "SELECT * FROM Appeals WHERE status = %s;"
    params = ('in_process',)
    return execute_query(query=query, params=params, fetch='all')


def get_my_all_appeals(uuid):
    query = "SELECT * FROM Appeals WHERE user_id = %s;"
    params = (uuid,)
    return execute_query(query=query, params=params, fetch='all')


def get_my_new_appeals(uuid):
    query = "SELECT * FROM Appeals WHERE user_id = %s AND status = %s;"
    params = (uuid, 'in_process')
    return execute_query(query=query, params=params, fetch='all')


def get_my_accepted_appeals(uuid):
    query = "SELECT * FROM Appeals WHERE user_id = %s AND status = %s;"
    params = (uuid, 'accepted')
    return execute_query(query=query, params=params, fetch='all')


def get_my_rejected_appeals(uuid):
    query = "SELECT * FROM Appeals WHERE user_id = %s AND status = %s;"
    params = (uuid, 'rejected')
    return execute_query(query=query, params=params, fetch='all')


def get_my_winner_appeals(uuid):
    query = "SELECT * FROM Appeals WHERE user_id = %s AND status = %s;"
    params = (uuid, 'winner')
    return execute_query(query=query, params=params, fetch='all')


def update_appeals(id, field, new_value):
    query = f"UPDATE Initiatives SET {field} = %s WHERE id = %s;"
    params = (new_value, id)
    execute_query(query=query, params=params)


def get_appeal_by_id(id):
    query = "SELECT * FROM Appeals WHERE id = %s;"
    params = (id,)
    return execute_query(query=query, params=params, fetch='one')
