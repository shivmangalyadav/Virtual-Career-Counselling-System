"""
DAL: Database Abstraction Layer
"""
from flask import session, jsonify
from .models import User
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import pymysql
import datetime

engine = create_engine(
    'mysql+pymysql://root:Shivam123@localhost:3306/virtual_counselling_system')
conn = pymysql.connect(
    'localhost',
    'root',
    'Shivam123',
    'virtual_counselling_system'
)
cur = conn.cursor()

Base = automap_base()
Base.prepare(engine, reflect = True)
User = Base.classes.vcadmin

f = Fernet('ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=')
ssn = Session(engine)

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
        pass

    def course_data(self):
        
        sql = """SELECT * FROM courses """
        cur.execute(sql)
        courses = cur.fetchall()
        cur.close()

        return courses


    def stream_data(self, cid):
        sql = """ SELECT StreamID FROM programs WHERE CourseID=%s """
        cur.execute(sql, cid)
        streams = cur.fetchall()

        streams_data = []
        sql = """ SELECT * FROM streams WHERE StreamID=%s """
        for i in streams:
            cur.execute(sql, i)
            streams_data.append(cur.fetchone())
        cur.close()

        return streams_data


    def program_data(self, cid, sid):
        sql = """ SELECT ProgramID, c.CourseID, CourseName, s.StreamID , StreamName FROM courses c inner join programs p on c.CourseID = p.CourseID inner join streams s on p.StreamID = s.StreamID WHERE c.CourseId=%s and s.StreamId=%s """
        cur.execute(sql, (cid, sid))
        data = cur.fetchall()
        cur.close()

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
        
        cur.execute(sql, pid)
        c_data = cur.fetchall()
        cur.close()

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
        
        cur.execute(sql, (pid, chid))
        c_data = cur.fetchall()
        cur.close()

        return c_data


class Admin:
    def __init__(self):
        pass

    def admin_login(self, email, psw):
        data = ssn.query(User).filter_by(AdminEmail = email).first()
        if data:
            # print(f.decrypt(data.AdminPassword.encode()).decode())
            # print(psw)
            if psw == f.decrypt(data.AdminPassword.encode()).decode():
                status = True
                session['logged_in'] = True
                session['Adminname'] = data.AdminName
                session['AdminEmail'] = data.AdminEmail
                
            else:
                status = False
        else:
            status = False
        ssn.close() 

        return status  


class AdminUniversity:
    def __init__(self):
       pass

    def fetch_univeristy_type(self):
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT DISTINCT UniversityType FROM universitydata")
        data = cur.fetchall()
        cur.close()
        
        return data


    def fetch_state(self):
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT DISTINCT State FROM universitydata")
        data = cur.fetchall()
        cur.close()

        return data


    def submit_university_data(self, name, address, state, Utype):
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute("INSERT INTO universitydata ( UniversityName, address, State, UniversityType, CreateDT) VALUES ( %s, %s, %s, %s, %s)", ((name, address, state, Utype, str(datetime.datetime.now()))))
            conn.commit()
            cur.close()
            
            return True
        except:
            return False


    def delete_data(self, name):
        cur = conn.cursor()
    
        try:
            data = cur.execute("DELETE from universitydata WHERE UniversityName=%s", (name))
            if data:
                conn.commit()
                cur.close()
                return True
            else:
                return False
            
        except:
            return False
        
    
class Users:
    def __init__(self):
        self.cur = conn.cursor(pymysql.cursors.DictCursor)

    def signin(self, data):
        self.cur.execute(
            "SELECT UserEmail, UserPassword from vcusers WHERE UserEmail=%s", (data['email'],))
        login_data = self.cur.fetchone()

        print(login_data)
        return login_data

    def signup(self, data, token):
        try:
            self.cur.execute("INSERT INTO vcusers (UserName, UserEmail, UserPassword)  VALUES (%s, %s, %s) ",
                        (data['name'], data['email'], token.decode()))
            msg = {"msg": 'Sign up successful!', 'status': True}
        except:
            msg = {"msg": 'email already exists.', 'status': False}
            return msg
        finally:
            conn.commit()
            # self.cur.close()
        return msg

    def profile(self, user_email):
        self.cur.execute(
            "SELECT UserEmail, UserName from vcusers WHERE UserEmail=%s", (user_email,))
        user_data = self.cur.fetchone()

        return user_data