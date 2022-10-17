import pandas as pd

dict = {"EMP 1" : {"Name":"John","Age":23,"gender":"Male"},
        "EMP 2": {"Name":"David","Age":26,"gender":"Male"},
        "EMP 3": {"Name":"Lisa","Age":22,"gender":"Female"}}

df = pd.DataFrame(dict)

df.to_csv("students2.csv",header=False, index= False)





# import pandas as pd
# import openpyxl
#
# a = [(12,34,45),
#      (34,56,67)]
#
# df1 = pd.DataFrame(a, columns=["a1","a2","a3"])
# #df = pd.read_csv()
# df = pd.read_excel("C:/Users/wscubetech/Desktop/school.xlsx","Sheet1")
#
# print(df1["a1"].mean())






# list1 = [("John",23,"Male"),("David",56,"Male")]
#
# dict = {"EMP 1" : {"Name":"John","Age":23,"gender":"Male"},
#         "EMP 2": {"Name":"David","Age":26,"gender":"Male"},
#         "EMP 3": {"Name":"Lisa","Age":22,"gender":"Female"}}
#
# df = pd.DataFrame(list1,columns=["emp1","emp2","emp3"])
# df1 = pd.DataFrame(dict)
# print(df1)


# avengers = ["ironman","hulk","hawkeye","thor"]
# marks = [98,76,56,34,89,67,78,35,60,98]
# s = pd.Series(marks)
# #print(s)
# #print(s.head(2))
# #print(s.tail(3))
# print(s.max())
# print(s.min())
# print(s.sum())
# print(s.mean())
