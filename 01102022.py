"""
press 1 to insert data
press 2 to delete data
press 3 to update data
press 4 to view data
"""



# import sqlite3
#
# conn = sqlite3.connect("student_data.db")
# cur = conn.cursor()
#
# get_data = cur.execute("""UPDATE STUDENTS SET NAME = "Pallav" WHERE ROLL_NO = 3 """)
#
# for i in get_data:
#     print(i)
#
# conn.commit()














# import sqlite3
#
# conn = sqlite3.connect("student_data.db")
# cur = conn.cursor()
#
# get_data = cur.execute("""DELETE FROM STUDENTS WHERE GRADE = "8th" """)
#
#
# conn.commit()





















# import sqlite3
#
# conn = sqlite3.connect("student_data.db")
# cur = conn.cursor()
#
# get_data = cur.execute("""SELECT * FROM STUDENTS WHERE GRADE = "8th" and ROLL_NO = "%s" """)
#
# cur.execute(get_data, roll_no)
# for i in get_data:
#     print(i)
#
# conn.commit()










#
# import sqlite3
#
# conn = sqlite3.connect("student_data.db")
# cur = conn.cursor()
# l = []
#
# while True:
#     name = input("enter name: ")
#     grade = input("enter grade: ")
#     email = input("enter email: ")
#     phone = int(input("enter phone number: "))
#     t = (name,grade,email,phone)
#
#     l.append(t)
#
#     data = """INSERT INTO STUDENTS
#     (NAME,GRADE,EMAIL,PHONE_NO)
#     VALUES(?,?,?,?)"""
#     repeat = input("repeat again?")
#     if repeat == "no":
#         break
#
# cur.executemany(data,l)
# conn.commit()
