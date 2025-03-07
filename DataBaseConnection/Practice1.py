import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="Anant@1080")

print(mydb)
# Verifying the connection
if mydb.open:
    print("Connection successful")
    print(f"Connected to: {mydb.get_host_info()}")
    print(f"Connected to: {mydb.get_autocommit()}")
    print(f"Connected to: {mydb.get_proto_info()}")
    print(f"Connected to: {mydb.get_host_info()}")
else:
    print("Connection failed")