import pymysql as mq

myobj = mq.connect(
    host="localhost",
    user="root",
    password="" 
)

cursor = myobj.cursor()

try:
    db = "CREATE DATABASE school"
    cursor.execute(db)
    print("Database has been created")
except:
    print("Database already exists or an error occurred")

cursor.close()
myobj.close()
