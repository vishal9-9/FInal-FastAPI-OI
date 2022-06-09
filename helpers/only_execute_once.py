import datetime
from database import engine
import bcrypt
from models.models import Company
from models import models
from helpers.passhash import genrate_hash_password

database = engine.session

models.Base.metadata.create_all(bind = engine.engine)

def initial_setup():
    psswd = '12345678'
    salt = bcrypt.gensalt()
    password = genrate_hash_password(psswd,salt).decode('utf-8')
    salt = salt.decode('utf-8')
    to_execute = database.query(Company).get(0)
    if not to_execute:
        c_query = f"insert into company (company_id, company_name, country, state, city, pincode, department, branch, address, isactive,created_at) values (0, 'SAdmin', 'SAdmin', 'SAdmin', 'SAdmin', '12345', 'SAdmin', 'SAdmin', 'SAdmin',1,'{datetime.datetime.now()}')"
        database.execute(c_query)
        database.commit()
        database.execute(f'update company set company_id = 0 where company_id = 1')
        database.commit()
        database.execute("insert into role (role_id,role_power) values (0,'Superadmin')")
        database.commit()
        database.execute("update role set role_id = 0 where role_id = 1")
        database.commit()
        database.execute("insert into role (role_id,role_power) values (1,'Admin'),(2,'Supervisor'),(3,'User')")
        database.commit()
        query = f'insert into users(c_id,fullname,email,password,contact_no,working_under,dob,isactive,role_id,created_at,salt) values(0,"SuperAdmin","super@admin.com","{password}","1234567890",0,"2000-08-13",1,0,"{datetime.datetime.now()}","{salt}")'
        database.execute(query)
        database.commit()
    else:
        print('initial setup not done')