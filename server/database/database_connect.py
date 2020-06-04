import pymysql
import itertools
import pandas as pd

conn = pymysql.connect(
    'localhost',
    'root',
    'Shivam123',
    'virtual_counselling_system'
)

class course_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, c_id, c_name):
        sql = """ INSERT INTO courses VALUES( %s, %s ) """
        self.cur.execute( sql, (c_id, c_name) )
        print(self.cur.rowcount , " row added.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM courses """ )
        data = self.cur.fetchall()

        print( data )

    def update(self, c_name, c_id):
        sql = """ UPDATE courses SET CourseName = %s WHERE CourseId = %s"""
        self.cur.execute(sql, (c_name, c_id))
        print(self.cur.rowcount , " row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM courses """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, c_id):
        sql = """ DELETE FROM courses WHERE CourseID = %s """
        self.cur.execute(sql, c_id)
        print(self.cur.rowcount , " row deleted.")
        conn.commit()

        self.cur.execute(""" SELECT * FROM courses """)
        data = self.cur.fetchall()

        print(data)

course = course_operation()
# course.insert(23, "new course")  
# course.update("23", 23)
# course.delete(23) 


class stream_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, s_id, s_name):
        sql = """ INSERT INTO streams VALUES( %s, %s ) """
        self.cur.execute( sql, (s_id, s_name) )
        print(self.cur.rowcount , " row added.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM streams """ )
        data = self.cur.fetchall()

        print( data )

    def update(self, s_name, s_id ):
        sql = """ UPDATE streams SET StreamName = %s WHERE StreamID = %s"""
        self.cur.execute(sql, (s_name, s_id))
        print(self.cur.rowcount , " row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM streams """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, s_id):
        sql = """ DELETE FROM streams WHERE StreamID = %s """
        self.cur.execute(sql, s_id)
        print(self.cur.rowcount , " row deleted.")
        conn.commit()

        self.cur.execute(""" SELECT * FROM streams """)
        data = self.cur.fetchall()

        print(data)

stream = stream_operation()
# stream.insert(1099, "OOO")
# stream.update("aaaaa", 1099)
# stream.delete(1099)

class program_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, p_id, c_id, s_id):
        sql = """ INSERT INTO programs VALUES( %s, %s, %s ) """
        self.cur.execute( sql, (p_id, c_id, s_id) )
        print(self.cur.rowcount , " row added.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM programs """ )
        data = self.cur.fetchall()

        print( data )

    def update(self, c_id, s_id, p_id):
        sql = """ UPDATE programs SET CourseID = %s, StreamID = %s WHERE ProgramID = %s"""
        self.cur.execute(sql, (c_id, s_id, p_id))
        print(self.cur.rowcount , " row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM programs """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, p_id):
        sql = """ DELETE FROM programs WHERE ProgramID = %s """
        self.cur.execute(sql, p_id)
        print(self.cur.rowcount , " row deleted.")
        conn.commit()

        self.cur.execute(""" SELECT * FROM programs """)
        data = self.cur.fetchall()

        print(data)

program = program_operation()
# program.insert(2000, 12, 200)
# program.update(1, 11, 2000)
# program.delete(2000)

class channel_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, ch_id, FP_id, TP_id):
        sql = """ INSERT INTO channel VALUES( %s, %s, %s ) """
        self.cur.execute( sql, (ch_id, FP_id, TP_id) )
        print(self.cur.rowcount , " row added.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM channel """ )
        data = self.cur.fetchall()

        print( data )

    def update(self, ch_id, FP_id, TP_id):
        sql = """ UPDATE channel SET FromProgramID = %s, ToProgramID = %s WHERE ChannelID = %s"""
        self.cur.execute(sql, (FP_id, TP_id, ch_id))
        print(self.cur.rowcount , " row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM channel """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, ch_id):
        sql = """ DELETE FROM channel WHERE ChannelID = %s """
        self.cur.execute(sql, ch_id)
        print(self.cur.rowcount , " row deleted.")
        conn.commit()

        self.cur.execute(""" SELECT * FROM channel """)
        data = self.cur.fetchall()

        print(data)

channel = channel_operation()
# channel.insert(20020, 12, 200)
# channel.update(20020, 1221, 22000)
# channel.delete(20020)


