import pymysql
import datetime

conn = pymysql.connect(
    'localhost',
    'root',
    'Lu9616@cky',
    'virtual_counselling_system'
)


def delete_data():

    cur = conn.cursor()

    sql = "DELETE FROM universitydata"
    cur.execute(sql)
    conn.commit()

    cur.close()
    # conn.close()


def append_data(data):
    data['CreateDT'] = str(datetime.datetime.now())
    cur = conn.cursor()

    query = """ INSERT INTO universitydata VALUES (%s, %s, %s, %s, %s, %s)"""
    cur.executemany(query, data.itertuples(index=True))
    conn.commit()

    cur.close()
    # conn.close()
