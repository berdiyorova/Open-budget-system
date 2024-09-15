from config.db_settings import execute_query


def add_vote(initiative_id , appeal_id, user_id):
    query = """INSERT INTO Votes 
                (initiative_id , appeal_id, user_id)
                VALUES (%s, %s, %s);
                """
    params = (initiative_id , appeal_id, user_id)
    execute_query(query=query, params=params)


def count_all_votes():
    query = """SELECT COUNT(*) FROM Votes;"""
    execute_query(query=query, fetch="one")


def count_votes_on_initiatives(initiative_id):
    query = """SELECT COUNT(*) FROM Votes WHERE initiative_id = %s;"""
    params = (initiative_id,)
    execute_query(query=query, params=params, fetch="all")


def count_votes_on_appeals(appeal_id):
    query = """SELECT COUNT(*) FROM Votes WHERE appeal_id = %s;"""
    params = (appeal_id,)
    execute_query(query=query, params=params, fetch="all")


def count_my_all_votes(user_id):
    query = """SELECT COUNT(*) FROM Votes WHERE user_id = %s;"""
    params = (user_id,)
    execute_query(query=query, params=params, fetch="all")


def get_my_voted_appeals(uuid):
    query = """
    SELECT
    """
