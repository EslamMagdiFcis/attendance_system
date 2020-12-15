from contextlib import closing

import sqlite3

DATABASE_PATH = "data/attendance.db"

def execute_query(sql_query):

    with sqlite3.connect(DATABASE_PATH) as con:

        with closing(con.cursor()) as cur:
            cur.execute(sql_query)
            query_set = cur.fetchall()

    return query_set
   