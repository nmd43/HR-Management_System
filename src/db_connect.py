import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raghav2007",
    database="hr_db")

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE feedback (index int NOT NULL AUTO_INCREMENT, content text, PRIMARY KEY(index) )")
mydb.commit()
my_cursor.close()
mydb.close()
