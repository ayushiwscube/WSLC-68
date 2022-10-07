#to delete data
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()
delete_data = cur.execute("delete from students where roll_no = 1")
mydb.commit()


#to update data
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()
update_data = cur.execute("""update students set branch = "electrical" where roll_no = 3 """)
mydb.commit()


#to get data
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()
get_data =("select * from students")
get_data = ("select * from students where age  = 23% ")
get_data = ("select * from students where branch like '%civil%' and age like '%23%' ")
cur.execute(get_data)

result = cur.fetchall()

for i in result:
    print(i)


#to insert data
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()
l = []
while True:
    roll = int(input("enter roll no: "))
    name = input("enter name: ")
    age = int(input("enter age: "))
    branch = input("enter branch: ")
    city = input("enter city: ")

    t = (roll,name,age,branch,city)
    l.append(t)

    query = "insert into students (roll_no,name,age,branch,city) values (%s,%s,%s,%s,%s)"
    cur.executemany(query,l)
    mydb.commit()

    repeat = input("repeat again? ")
    if repeat == "no":
        break


#to insert data without user input
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()

cur.execute("insert into students (roll_no,name,age,branch,city) values (1,"john",19,"civil","Jodhpur") ")

mydb.commit()

#to create table
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "college")
cur = mydb.cursor()

data = "create table if not exists students (roll_no int(5) primary key, name varchar(30) not null,age int(2) not null, branch varchar(30) not null,city varchar(30) not null) "

cur.execute(data)



#to show all the databases
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345")
cur = mydb.cursor()
cur.execute("show databases")

for i in cur:
    print (i)



#to create a database
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "12345")
cur = mydb.cursor()
cur.execute("""create database college""")
