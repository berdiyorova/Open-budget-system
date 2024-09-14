import json

from config.db_settings import execute_query


def insert_districts():
    if not get_all_districts():
        with open('utils/districts.json', 'r') as file:
            districts = json.load(file)

        for district in districts:
            region_id = district['region_id']
            name = district['name']
            query = "INSERT INTO Districts (region_id, name) VALUES (%s, %s);"
            execute_query(query=query, params=(region_id, name))


def get_all_districts():
    query = "SELECT * FROM Districts;"
    return execute_query(query=query, fetch='all')


def get_districts(region_id):
    query = "SELECT id, name FROM Districts WHERE region_id = %s;"
    return execute_query(query=query, params=(region_id,), fetch='all')
