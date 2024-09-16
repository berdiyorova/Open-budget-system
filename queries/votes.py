from config.db_settings import execute_query


def add_vote(initiative_id, appeal_id, email) -> None:
    query = """INSERT INTO Votes 
                (initiative_id , appeal_id, email)
                VALUES (%s, %s, %s);
                """
    params = (initiative_id, appeal_id, email)
    execute_query(query=query, params=params)


def count_all_votes():
    query = """SELECT COUNT(*) FROM Votes;"""
    return execute_query(query=query, fetch="one")


def count_votes_on_initiatives(initiative_id):
    query = """SELECT COUNT(*) FROM Votes WHERE initiative_id = %s;"""
    params = (initiative_id,)
    return execute_query(query=query, params=params, fetch="all")


def count_votes_on_appeal(appeal_id):
    query = """SELECT COUNT(*) FROM Votes WHERE appeal_id = %s;"""
    params = (appeal_id,)
    return execute_query(query=query, params=params, fetch="all")


def get_my_voted_appeals(email):
    query = """
        SELECT a.title, i.name 
        FROM Appeals a  
        JOIN Votes v ON a.id = v.appeal_id  
        JOIN Initiatives i ON a.initiative_id = i.id  
        WHERE v.email = %s;  
        """
    params = (email,)
    return execute_query(query=query, params=params, fetch="all")


def get_users_voted_on_appeal(appeal_id):
    query = """
        SELECT DISTINCT v.email 
        FROM Votes v  
        JOIN Appeals a ON v.appeal_id = a.id  
        WHERE a.id = %s;  
        """
    params = (appeal_id,)
    return execute_query(query=query, params=params, fetch="all")


def get_appeals_with_the_most_votes():
    query = """
        SELECT a.id, a.title, COUNT(v.id) AS total_votes  
        FROM Appeals a  
        LEFT JOIN Votes v ON a.id = v.appeal_id  
        GROUP BY a.id  
        ORDER BY total_votes DESC  
        LIMIT 50;
        """
    return execute_query(query=query, fetch='all')


def get_appeals_with_the_most_votes_on_initiative(initiative_id):
    query = """
        SELECT   
            i.id,   
            a.id,   
            a.title,   
            COUNT(v.id) AS total_votes  
        FROM Initiatives i  
        JOIN Appeals a ON i.id = a.initiative_id  
        LEFT JOIN Votes v ON a.id = v.appeal_id  
        WHERE i.id = %s
        GROUP BY i.id, a.id  
        ORDER BY total_votes DESC  
        LIMIT 50;
        """
    params = (initiative_id,)
    return execute_query(query=query, params=params, fetch='all')
