from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker
import pymysql

conn = pymysql.connect(
    'localhost',
    'root',
    'Lu9616@cky',
    'virtual_counselling_system'
)

engine = create_engine('mysql+pymysql://root:Lu9616@cky@localhost:3306/vccs', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()

# region Models
# * Here we're defining all of our Models,
# * namely: User, Follower, Post, Reaction


class User(Base):
    __tablename__ = 'vcusers'

    UserEmail = Column(String(50), primary_key=True)
    UserName = Column(String(50), nullable=False)
    UserPassword = Column(String(500), nullable=False)
    JoiningDT = Column(DateTime, default=datetime.datetime.utcnow)
    UserDOB = Column(Date, nullable=True)
    UserGender = Column(String(10), nullable=True)
    UserPhone = Column(String(20), nullable=True)
    UserAddress = Column(Text, nullable=True)
    UserCountry = Column(String(20), nullable=True)
    UserState = Column(String(20), nullable=True)
    UserCity = Column(String(20), nullable=True)
    UserZipcode = Column(Integer, nullable=True)
    UserCreatedOn = Column(DateTime, default=datetime.datetime.utcnow)
    UserIsActivated = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    CreateDate = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    UpdateData = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    UserProfilePic = Column(String(200), nullable=True)

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)


class Admin(Base):
    __tablename__ = 'vcadmin'

    AdminEmail = Column(String(50), primary_key=True)
    AdminName = Column(String(50), nullable=False)
    AdminPassword = Column(String(500), nullable=False)
    JoiningDT = Column(DateTime, default=datetime.datetime.utcnow)


    def __repr__(self):
        return "<User(email='%s')>" % (self.email)


class UniversityData(Base):
    __tablename__ = 'universitydata'

    UniversityID = Column(Integer, primary_key=True)
    UniversityName = Column(Text, nullable=False)
    Address = Column(Text, nullable=False)
    State = Column(String(50), nullable=False)
    UniversityType = Column(String(70), nullable=False)
    CreateDT = Column(DateTime, default=datetime.datetime.utcnow)


class Channel(Base):
    __tablename__ = 'channel'

    ChannelID = Column(Integer, primary_key=True)
    FromProgramID = Column(Integer, nullable=False)
    ToProgramID = Column(Integer, nullable=False)


class Course(Base):
    __tablename__ = 'courses'

    CourseID = Column(Integer, primary_key=True)
    CourseName = Column(String(50), nullable=False)


class Stream(Base):
    __tablename__ = 'streams'

    StreamID = Column(Integer, primary_key=True)
    StreamName = Column(String(50), nullable=False)

class Program(Base):
    __tablename__ = 'programs'

    ProgramID = Column(Integer, primary_key=True)
    CourseID = Column(Integer, nullable=False)
    StreamID = Column(Integer, nullable=False)




# # INSERT, DELETE, UPDATE Operations in stream, course, program table

class course_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, c_id, c_name):
        sql = """ INSERT INTO courses VALUES( %s, %s ) """
        self.cur.execute( sql, (c_id, c_name) )
        print(self.cur.rowcount , "row added.")
        conn.commit()

        self.cur.execute( """SELECT * FROM courses""" )
        data = self.cur.fetchall()

        print( data )

    def update(self, c_name, c_id):
        sql = """ UPDATE courses SET CourseName = %s WHERE CourseId = %s"""
        self.cur.execute(sql, (c_name, c_id))
        print(self.cur.rowcount , "row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM courses """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, c_id):
        sql = """ DELETE FROM courses WHERE CourseID = %s """
        self.cur.execute(sql, c_id)
        print(self.cur.rowcount , "row deleted.")
        conn.commit()

        self.cur.execute(""" SELECT * FROM courses """)
        data = self.cur.fetchall()

        print(data)

# course = course_operation()
# course.insert(23, "new course")  
# course.update("23", 23)
# course.delete(23) 


class stream_operation:
    def __init__(self):
        self.cur = conn.cursor()

    def insert(self, s_id, s_name):
        sql = """ INSERT INTO streams VALUES( %s, %s ) """
        self.cur.execute( sql, (s_id, s_name) )
        print(self.cur.rowcount , "row added.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM streams """ )
        data = self.cur.fetchall()

        print( data )

    def update(self, s_name, s_id ):
        sql = """ UPDATE streams SET StreamName = %s WHERE StreamID = %s"""
        self.cur.execute(sql, (s_name, s_id))
        print(self.cur.rowcount , "row updated.")
        conn.commit()

        self.cur.execute( """ SELECT * FROM streams """ )
        data = self.cur.fetchall()

        print( data )

    def delete(self, s_id):
        sql = """ DELETE FROM streams WHERE StreamID = %s """
        self.cur.execute(sql, s_id)
        print(self.cur.rowcount , "row deleted.")
        conn.commit()

        self.cur.execute("""SELECT * FROM streams """)
        data = self.cur.fetchall()

        print(data)

# stream = stream_operation()
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

        self.cur.execute( """SELECT * FROM programs """ )
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

# program = program_operation()
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

        self.cur.execute( """SELECT * FROM channel """ )
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

# channel = channel_operation()
# channel.insert(20020, 12, 200)
# channel.update(20020, 1221, 22000)
# channel.delete(20020)


def main():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
