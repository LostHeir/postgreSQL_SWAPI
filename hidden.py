def secrets():
    return {"host": "pg.pg4e.com",
            "port": 5432,
            "database": "pg4e_010b0b42de",
            "user": "pg4e_010b0b42de",
            "pass": "pg4e_p_3b5bff6c57f428e"}

# Return a psycopg2 connection string
# 'dbname=pg4e_data user=pg4e_data_read password=pg4e_p_d5fab7440699124 host=pg.pg4e.com port=5432'


def psycopg2(secrets):
     return ('dbname='+secrets['database']+' user='+secrets['user'] +
        ' password='+secrets['pass']+' host='+secrets['host'] +
        ' port='+str(secrets['port']))
