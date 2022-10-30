import mysql.connector

cnx = mysql.connector.connect(user='root', password='sql_1234', host='127.0.0.1', database='password_generated')

cur = cnx.cursor()

cur.execute("INSERT INTO passwords(title,password_gen) VALUE ('test1','password')")

records = cur.fetchall()

# for row in records:
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print("\n")

cnx.close()