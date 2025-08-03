# E-mail Slicer
#--------------

import re

email = input("Enter E-mail: ").strip()

# Simple validation using regex
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    username, domain = email.split('@')
    print('Valid Email!')
    print('Username :', username)
    print('Domain   :', domain)
else:
    print('Invalid Email!')
