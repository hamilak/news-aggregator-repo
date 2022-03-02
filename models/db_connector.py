import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kal20imah00.",
)

cursor = db.cursor()
# cursor.execute("show databases")
# print(db)