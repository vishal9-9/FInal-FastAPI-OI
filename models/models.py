from database.engine import Base
from sqlalchemy import Column ,Integer ,String ,ForeignKey ,Date , TIMESTAMP 

class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer,primary_key = True,nullable=False)
    company_name = Column(String(100),nullable=False,unique=True)
    country = Column(String(75),nullable=False)
    state = Column(String(75),nullable=False)
    city = Column(String(75),nullable=False)
    pincode = Column(String(15),nullable=False)
    department = Column(String(50),nullable=False)
    branch = Column(String(75),nullable=False)
    address = Column(String(250),nullable=False)
    created_at = Column(TIMESTAMP,nullable=False)
    updated_at = Column(TIMESTAMP)
    isactive = Column(Integer,nullable=False)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    c_id = Column(Integer, ForeignKey('company.company_id'))
    fullname = Column(String(75),nullable=False)
    email = Column(String(50),unique=True,nullable=False)
    password = Column(String(250),nullable=False)
    salt = Column(String(100),nullable=False)
    contact_no = Column(String(16),nullable=False)
    working_under = Column(Integer,nullable=False)
    dob = Column(Date,nullable=False)
    created_at = Column(TIMESTAMP,nullable=False)
    updated_at = Column(TIMESTAMP)
    isactive = Column(Integer,nullable=False)
    role_id = Column(Integer,ForeignKey('role.role_id'))

class Role(Base):
    __tablename__ = 'role'
    role_id = Column(Integer,primary_key=True,nullable=False)
    role_power = Column(String(20),nullable=False,unique=True)