import os
import hashlib

def login(password):
    # VULNERABILITY: Using weak hashing algorithm (MD5)
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    
    # VULNERABILITY: Hardcoded secret
    if m.hexdigest() == "5f4dcc3b5aa765d61d8327deb882cf99": 
        return True
    
    # SMELL: Use of 'eval' is a massive security risk
    user_input = "print('Hello')"
    eval(user_input) 
    
    return False
