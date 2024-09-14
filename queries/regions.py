import json

from config.db_settings import execute_query

import json


def insert_regions():
    if not get_regions():
        with open('utils/regions.json', 'r') as file:
            regions = json.load(file)

        for region in regions:
            name = region['name']
            query = "INSERT INTO Regions (name) VALUES (%s);"
            execute_query(query=query, params=(name,))


def get_regions():
    query = "SELECT * FROM Regions;"
    return execute_query(query=query, fetch='all')
