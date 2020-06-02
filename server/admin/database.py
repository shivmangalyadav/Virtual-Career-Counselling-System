from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import pymysql
import datetime

engine = create_engine(
    'mysql+pymysql://root:Shivam123@localhost:3306/virtual_counselling_system')
Base = automap_base()
Base.prepare(engine, reflect = True)

conn = pymysql.connect(
            'localhost',
            'root',
            'Shivam123',
            'virtual_counselling_system'
        ) 

User = Base.classes.vcadmin



def fetch_univeristy_type():
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT DISTINCT UniversityType FROM universitydata")
    data = cur.fetchall()
    cur.close()
    
    return data


def fetch_state():
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT DISTINCT State FROM universitydata")
    data = cur.fetchall()
    cur.close()

    return data


def submit_university_data(name, address, state, Utype):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute("INSERT INTO universitydata ( UniversityName, address, State, UniversityType, CreateDT) VALUES ( %s, %s, %s, %s, %s)", ((name, address, state, Utype, str(datetime.datetime.now()))))
        conn.commit()
        cur.close()
        
        return True
    except:
        return False


def delete_data(name):
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
    
    
