import mysql.connector

myconn=mysql.connector.connect(host="localhost",username="root",password="Anant@1080",database="sample")

print(myconn)

cursor=myconn.cursor()
# cursor.execute("show databases")
# cursor.execute(" create database sample")
# cursor.execute("show tables")
# cursor.execute("create table studinfo(sid int,sname varchar(50),smarks int,smobilenumber bigint)")
# cursor.execute("show tables")
# print("Database created successfully")
# print("Table created successfully")

# cursor.execute("insert into studinfo values(1,'Anant Khutale',90,989023332)")
# cursor.execute("insert into studinfo(sid,sname,smarks,smobilenumber) values(1,'Anant Khutale',90,989023332),(2,'Sachin Kadam',75,9764751008)")
# cursor.execute("delete from studinfo where sname='Sachin Kadam'")
# cursor.execute("update studinfo set smobilenumber=9890129062 where sname='Sachin Kadam'")
# cursor.execute("update studinfo set sid=1, sname='ABCD',smarks=50,smobilenumber=9890909090 where smarks=90")
# cursor.execute("update studinfo set sid=4,sname='PQRS',smarks=45 where smobilenumber=9890129062")
# cursor.execute("select * from studinfo where sid=1")

# cursor.execute("alter table studinfo add column semail varchar(50)")
# cursor.execute("update studinfo set semail='Anant@gmail.com' where sid>0 and sid<5")
# cursor.execute("update studinfo set semail='Sachin@gmail.com' where sid=4")
# cursor.execute("alter table studinfo modify column sid smallint")
# cursor.execute("describe studinfo")
# cursor.execute("alter table studinfo drop column smarks")
# cursor.execute("alter table studentsdetails rename to studinfo")
# cursor.execute("insert into studinfo values(3,'Arnav Patil',99,9922992262)")
# cursor.execute("delete from studinfo where sid=3")
# cursor.execute("delete from studinfo")
myconn.commit()

# print("Data inserted successfully")
# cursor.execute("select * from students")
# cursor.execute("select * from students where Name='Alice Johnson'")
result=cursor.fetchall()

print(result)
cursor.close()
myconn.close()
