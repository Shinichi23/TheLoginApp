import hashlib
import os
import base64

def generate_salt():
    salt = os.urandom(16)
    return base64.b64encode(salt).decode('utf-8')

def hash_password(password, salt):
    password_bytes = password.encode('utf-8')
    salt_bytes = base64.b64decode(salt)

    salted_password = salt_bytes + password_bytes
    hash_obj = hashlib.sha256(salted_password)

    return hash_obj.hexdigest()

def verify_password(stored_password, salt, password_attempt):
    
    attempt_hash = hash_password(password_attempt, salt)

    return stored_password == attempt_hash