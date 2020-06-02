from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:Shivam123@localhost:3306/vccs', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()

# region Models
# * Here we're defining all of our Models,
# * namely: User, Follower, Post, Reaction


class User(Base):
    # def __init__(self, email, firstName, middleName, lastName, phone):
    #     self.email = email
    #     self.firstName = firstName
    #     self.middleName = middleName
    #     self.lastName = lastName
    #     self.phone = phone

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
    def __init__(self, email, name, password):
        self.AdminEmail = email
        # self.AdminName = name
        # self.AdminPassword = password
        # self.JoiningDT = joindt


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

# * Models declaration ends
# endregion


def main():
    # email = Admin("dhibjbd@sdii", "shiva", 'kumar')
    # print("=-=------------------")
    # print(repr(email))
    # print("=-=------------------")

    # session.add(email)
    # session.commit()
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
