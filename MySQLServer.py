import mysql.connector
from mysql.connector import Error


mydb = None
cursor = None

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="hooyo",
        database="alx_book_store"
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")

