from config.db_settings import execute_query


def add_appeal(user_id, category_id, region_id, district_id, title, funds_offered):
    query = """INSERT INTO Appeals 
                (user_id, category_id, region_id, district_id, title, funds_offered)
                VALUES (%s, %s, %s, %s, %s, %s);
                """
    params = (user_id, category_id, region_id, district_id, title, funds_offered)
    execute_query(query=query, params=params)
