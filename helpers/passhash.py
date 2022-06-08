import bcrypt

def genrate_hash_password(password,salt):
    hashed_password = bcrypt.hashpw(password,salt)
    return hashed_password

def check_hash(password,hash):
    return bcrypt.checkpw(password.encode('utf-8'),hash.encode('utf-8'))
    