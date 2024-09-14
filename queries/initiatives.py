from config.db_settings import execute_query


def add_initiative(name, application_period, moderation_period, voting_period, allocated_funds):
    query = """INSERT INTO Initiatives 
                (name, application_period, moderation_period, voting_period, allocated_funds)
                VALUES (%s, %s, %s, %s, %s);
                """
    params = (name, application_period, moderation_period, voting_period, allocated_funds)
    execute_query(query=query, params=params)
