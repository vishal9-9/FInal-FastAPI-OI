import bcrypt

def genrate_hash_password(password: str,salt):
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password,salt)
    return hashed_password

def check_hash(password: str,hash: str):
    return bcrypt.checkpw(password.encode(),hash.encode())
    