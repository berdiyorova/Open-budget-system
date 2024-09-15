from config.db_settings import execute_query


def add_vote(initiative_id, appeal_id, user_id):
    query = """INSERT INTO Votes 
                (initiative_id , appeal_id, user_id)
                VALUES (%s, %s, %s);
                """
    params = (initiative_id, appeal_id, user_id)
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
        SELECT a.title, i.name 
        FROM Appeals a  
        JOIN Votes v ON a.id = v.appeal_id  
        JOIN Initiatives i ON a.initiative_id = i.id  
        WHERE v.user_id = %s;  
        """
    params = (uuid,)
    execute_query(query=query, params=params, fetch="all")


def get_users_voted_on_appeal(appeal_id):
    query = """
        SELECT DISTINCT u.first_name, u.last_name, u.phone 
        FROM Users u  
        JOIN Votes v ON u.uuid = v.user_id  
        JOIN Appeals a ON v.appeal_id = a.id  
        WHERE a.id = %s;  
        """
    params = (appeal_id,)
    execute_query(query=query, params=params, fetch="all")


def get_appeals_with_the_most_votes():
    query = """
        SELECT a.id, a.title, COUNT(v.id) AS total_votes  
        FROM Appeals a  
        LEFT JOIN Votes v ON a.id = v.appeal_id  
        GROUP BY a.id  
        ORDER BY total_votes DESC  
        LIMIT 10;
        """
    execute_query(query=query, fetch='all')


def get_appeals_with_the_most_votes_within_initiative(initiative_id):
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
        LIMIT 10;
        """
    params = (initiative_id,)
    execute_query(query=query, params=params, fetch='all')
