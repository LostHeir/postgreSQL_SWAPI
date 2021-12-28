# python3 swapi.py
# Pulls data from the swapi.py4e.com API and puts it into swapi table

import hidden
import myutils
import psycopg2
import time
import json
import requests


def summary(cur):
    total = myutils.query_value(cur, 'SELECT COUNT(*) FROM swapi;')
    todo = myutils.query_value(cur, 'SELECT COUNT(*) FROM swapi WHERE status IS NULL;')
    good = myutils.query_value(cur, 'SELECT COUNT(*) FROM swapi WHERE status = 200;')
    error = myutils.query_value(cur, 'SELECT COUNT(*) FROM swapi WHERE status != 200;')
    print(f'Total={total} todo={todo} good={good} error={error}')


# Loads the secrets
secrets = hidden.secrets()

conn = psycopg2.connect(host=secrets['host'],
                        port=secrets['port'],
                        database=secrets['database'],
                        user=secrets['user'],
                        password=secrets['pass'],
                        connect_timeout=3)
