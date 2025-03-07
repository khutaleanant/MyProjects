import pymysql

# Establish connection
conn = pymysql.connect(
    host="localhost",        # Example: "localhost" or an IP address
    user="root",    # Example: "root"
    password="Anant@1080", # Your MySQL password
    database="xyz_traning_center" # The database you want to work with
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Execute a query (for example, fetching all rows from both tables)
cursor.execute("SELECT * FROM students")  # Execute the first query
results = cursor.fetchall()  # Fetch all results

# Print results from the first query
print("Students Table:")
for row in results:
    print(row)

# Execute the second query (fetching from the 'course' table)
cursor.execute("SELECT * FROM courses")
results = cursor.fetchall()  # Fetch all results for the second query

# Print results from the second query
print("\nCourse Table:")
for row in results:
    print(row)

##====================================================================================
 # Insert 5 new rows into the 'students' table

    Insert_Query = [
    "INSERT INTO students (StudentID,Name,Email) VALUES (1001,'Arnav','Arnav@gmail.com')",
    "INSERT INTO students (StudentID,Name,Email) VALUES (2001,'Aarav','Aarav@gmail.com')",
    "INSERT INTO students (StudentID,Name,Email) VALUES (3001,'Shardul','Shardul@gmail.com')",
    "INSERT INTO students (StudentID,Name,Email) VALUES (4001,'Samrudhi','Samrudhi@gmail.com')"
]


#Execute each insert query
for query in Insert_Query:
    cursor.execute(query)

# Commit the changes to the database
conn.commit()

print(cursor.rowcount,"Successfully updated 4 rows and inserted 5 new rows into the 'students' table.")

# Close the cursor and connection
cursor.close()
conn.close()