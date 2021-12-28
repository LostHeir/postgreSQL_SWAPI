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

cur = conn.cursor()

print('# ------------------------------------------- #')
print('# --- To restart the spider, run: ----------- #')
print('# --- DROP TABLE IF EXISTS swapi CASCADE; --- #')
print('# ------------------------------------------- #')

sql = '''
CREATE TABLE IF NOT EXISTS swapi
(id serial, url VARCHAR(2048) UNIQUE, status INTEGER, body JSONB,
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), updated_at TIMESTAMPTZ);
'''

print(sql)
cur.execute(sql)

# Check if table already have some urls, if not add stating points
sql = 'SELECT COUNT(url) FROM swapi;'
count = myutils.query_value(cur, sql)
if count < 1:
    objects = ['films', 'species', 'people']
    for obj in objects:
        sql = f"INSERT INTO swapi (url) VALUES ('https://swapi.dev/api/{obj}/1/' );"
        print(sql)
        cur.execute(sql)
    conn.commit()

many = 0
count = 0
chars = 0
fail = 0
summary(cur)
