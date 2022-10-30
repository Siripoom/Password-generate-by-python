#import module
from functools import update_wrapper
import random
import string
from unittest import result
import mysql.connector

#input length of password
def gen(length):
    
    #or define length
    #length = 16
    #define data
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    symbols = string.punctuation

    #combine
    all = upper + lower + number + symbols

    ran = random.sample(all,length)

    password = "".join(ran)

    print("Password:",password)

"""a = int(input())
a = gen(a)
print( a )"""

# Database Mysql
cnx = mysql.connector.connect(user='root', password='sql_1234', host='127.0.0.1', database='password_generated')

cur = cnx.cursor()

cur.execute("SELECT * FROM passwords")

records = cur.fetchall()

for row in records:
    print(row[0])
    print(row[1])
    print(row[2])
    print("\n")

cnx.close()