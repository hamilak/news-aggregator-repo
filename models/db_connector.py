import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kal20imah00.",
    database="database"
)


cursor = db.cursor()
# cursor.execute("create database user")
# for i in cursor:
#     print(i)
# print(db)

