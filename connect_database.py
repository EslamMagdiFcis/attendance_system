from contextlib import closing

import sqlite3


def execute_query(databse_path, sql_query):

    with sqlite3.connect(databse_path) as con:

        with closing(con.cursor()) as cur:
            cur.execute(sql_query)
            query_set = cur.fetchall()

    return query_set
   