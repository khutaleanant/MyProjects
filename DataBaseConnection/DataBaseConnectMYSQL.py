# Importing module
import mysql.connector

try:
    # Establishing the connection inside the try block
    MyDB = mysql.connector.connect(host="localhost", user="root", password="Anant@1080")

    # Printing the connection object
    print(MyDB)

    # If successful
    print("Connected to database successfully!")
    
except mysql.connector.Error as e:
    # Handling errors for MySQL connection
    print(f"Error: {e}")
