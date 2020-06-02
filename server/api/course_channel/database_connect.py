import pymysql
import itertools
import pandas as pd

conn = pymysql.connect(
    'localhost',
    'root',
    'Shivam123',
    'virtual_counselling_Final'
)

def course_data():
    cur = conn.cursor()
    sql = """SELECT * FROM courses """
    cur.execute(sql)
    courses = cur.fetchall()
    # conn.commit()

    return courses

    # cur.close()
    # conn.close


def stream_data(cid):
    cur = conn.cursor()
    sql = """ SELECT StreamID FROM programs WHERE CourseID=%s """
    cur.execute(sql, cid)
    streams = cur.fetchall()

    streams_data = []
    sql = """ SELECT * FROM streams WHERE StreamID=%s """
    for i in streams:
        cur.execute(sql, i)
        streams_data.append(cur.fetchone())

    return streams_data


def program_data(cid, sid):
    cur = conn.cursor()

    sql = """ SELECT ProgramID, c.CourseID, CourseName, s.StreamID , StreamName FROM courses c inner join programs p on c.CourseID = p.CourseID inner join streams s on p.StreamID = s.StreamID WHERE c.CourseId=%s and s.StreamId=%s """
    cur.execute(sql, (cid, sid))
    data = cur.fetchall()
    # print(data)

    return data


def channel_data(pid):
    cur = conn.cursor()
    # sql = """ SELECT FromProgramID, ToProgramID FROM channel WHERE FromProgramID = %s """
    sql = """SELECT c.ChannelID, c1.CourseID, c1.CourseName, s.StreamID, s.StreamName 
            FROM programs p 
            inner join channel c on c.FromProgramID = p.ProgramID 
            inner join programs p1 on c.ToProgramID = p1.ProgramID  
            inner join courses c1 on c1.CourseID = p1.CourseID 
            inner join streams s on s.StreamID = p1.StreamID
            WHERE p.ProgramID=%s
        """
    
    cur.execute(sql, pid)
    c_data = cur.fetchall()

    return c_data


def single_channel_data(pid, chid):
    cur = conn.cursor()
    # sql = """ SELECT FromProgramID, ToProgramID FROM channel WHERE FromProgramID = %s """
    sql = """SELECT c.ChannelID, c1.CourseID, c1.CourseName, s.StreamID, s.StreamName 
            FROM programs p 
            inner join channel c on c.FromProgramID = p.ProgramID 
            inner join programs p1 on c.ToProgramID = p1.ProgramID  
            inner join courses c1 on c1.CourseID = p1.CourseID 
            inner join streams s on s.StreamID = p1.StreamID
            WHERE p.ProgramID=%s and c.ChannelID = %s
        """
    
    cur.execute(sql, (pid, chid))
    c_data = cur.fetchall()

    return c_data


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

    def update(self, c_name, c_id ):
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
# course.insert()  
# course.update()
# course.delete() 


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


