"""
DAL: Database Abstraction Layer
"""

from .models import User
import pymysql
import itertools
import pandas as pd


conn = pymysql.connect(
    'localhost',
    'root',
    'Shivam123',
    'virtual_counselling_system'
)


def user_signup(user: User) -> bool:
    pass

def user_signin(loginId: str, password: str) -> bool:
    pass

def get_user_info(systemUserId: int) -> User:
    print(User)
    return "nff"

def users_list() -> list:
    pass


class Course:
    def __init__(self):
        self.cur = conn.cursor()

    def course_data(self):
        
        sql = """SELECT * FROM courses """
        self.cur.execute(sql)
        courses = self.cur.fetchall()

        return courses

        # cur.close()
        # conn.close

    def stream_data(self, cid):
        sql = """ SELECT StreamID FROM programs WHERE CourseID=%s """
        self.cur.execute(sql, cid)
        streams = self.cur.fetchall()

        streams_data = []
        sql = """ SELECT * FROM streams WHERE StreamID=%s """
        for i in streams:
            self.cur.execute(sql, i)
            streams_data.append(self.cur.fetchone())

        return streams_data


    def program_data(self, cid, sid):
        sql = """ SELECT ProgramID, c.CourseID, CourseName, s.StreamID , StreamName FROM courses c inner join programs p on c.CourseID = p.CourseID inner join streams s on p.StreamID = s.StreamID WHERE c.CourseId=%s and s.StreamId=%s """
        self.cur.execute(sql, (cid, sid))
        data = self.cur.fetchall()

        return data


    def channel_data(self, pid):
        # sql = """ SELECT FromProgramID, ToProgramID FROM channel WHERE FromProgramID = %s """
        sql = """SELECT c.ChannelID, c1.CourseID, c1.CourseName, s.StreamID, s.StreamName 
                FROM programs p 
                inner join channel c on c.FromProgramID = p.ProgramID 
                inner join programs p1 on c.ToProgramID = p1.ProgramID  
                inner join courses c1 on c1.CourseID = p1.CourseID 
                inner join streams s on s.StreamID = p1.StreamID
                WHERE p.ProgramID=%s
            """
        
        self.cur.execute(sql, pid)
        c_data = self.cur.fetchall()

        return c_data


    def single_channel_data(self, pid, chid):
        # sql = """ SELECT FromProgramID, ToProgramID FROM channel WHERE FromProgramID = %s """
        sql = """SELECT c.ChannelID, c1.CourseID, c1.CourseName, s.StreamID, s.StreamName 
                FROM programs p 
                inner join channel c on c.FromProgramID = p.ProgramID 
                inner join programs p1 on c.ToProgramID = p1.ProgramID  
                inner join courses c1 on c1.CourseID = p1.CourseID 
                inner join streams s on s.StreamID = p1.StreamID
                WHERE p.ProgramID=%s and c.ChannelID = %s
            """
        
        self.cur.execute(sql, (pid, chid))
        c_data = self.cur.fetchall()

        return c_data

