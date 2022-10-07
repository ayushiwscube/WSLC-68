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

    query = "insert into students (roll_no,name,age,branch,city) values (?,?,?,?,?)"
    cur.executemany(query,l)
    mydb.commit()

    repeat = input("repeat again? ")
    if repeat == "no":
        break

    
#cur.execute("insert into students (roll_no,name,age,branch,city) values (1,"john",19,"civil","Jodhpur") ")

#mydb.commit()


"""
data = "create table if not exists students (roll_no int(5) primary key, name varchar(30) not null,age int(2) not null, branch varchar(30) not null,city varchar(30) not null) "

cur.execute(data)




cur.execute("show databases")

for i in cur:
    print (i)

"""



#cur.execute("""create database college""")
