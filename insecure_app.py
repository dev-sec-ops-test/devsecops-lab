import os
import subprocess

# 1️⃣ Hardcoded password (Security Vulnerability)
password = "admin123"

# 2️⃣ Hardcoded secret key
SECRET_KEY = "mysecretkey"

# 3️⃣ SQL Injection vulnerability
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    print("Executing query:", query)

# 4️⃣ Command Injection vulnerability
def run_command(user_input):
    os.system("echo " + user_input)

# 5️⃣ Using subprocess unsafely
def run_process(user_input):
    subprocess.call("ls " + user_input, shell=True)

# 6️⃣ Unused variable (Code Smell)
unused_variable = "I am not used"

# 7️⃣ Function too complex (Code Smell)
def complex_function(a, b, c, d, e, f):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            print("Too many nested conditions!")

# 8️⃣ Weak hashing algorithm (Security issue)
import hashlib
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

print("App loaded")
