import sqlite3

conn = sqlite3.connect("student_data.db")
cur = conn.cursor()

student = """ CREATE TABLE IF NOT EXISTS STUDENTS
(ROLL_NO INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(255) NOT NULL,
GRADE VARCHAR(255) NOT NULL,
EMAIL VARCHAR(255) NOT NULL,
PHONE_NO INTEGER NOT NULL) """

cur.execute(student)
conn.commit()





















# class smartphone:
#     def oneplus(self):
#         print ("Oneplus 8 pro")
#
# class phone(smartphone):
#     def oneplus(self):
#         super().oneplus()
#         print ("Oneplus 9 R")
#
# obj = phone()
# obj.oneplus()





# class companyA:
#     def employee1(self):
#         print("the name of the employee is John")
#
# class companyB(companyA):
#     def employee1(self):
#         super().employee1()
#         print("the name of the employee is Maria")
#
# obj = companyB()
# obj.employee1()

























# class Employee:
#     def emp1(self,name =""):
#         print ("the name of the employee is", name)
#
# e = Employee()
# e.emp1("John")














# class Employee:
#     def set_emp_name(self,name):
#         self.__name = name
#     def get_emp_name(self):
#         return self.__name
#
#     def emp_data(self):
#         print("the name of the employee is",self.__name)
#
# emp = Employee()
# emp.set_emp_name("john")
# emp.emp_data()

