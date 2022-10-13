import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [30,40,50,45,60]
y1 = [10,60,30,50,80]

plt.plot(x,y,label = "men", linestyle = ":", color = "red",marker = "^",mec = "black")
plt.plot(x,y1, label = "women", linewidth =2, color = "green",marker = "o")
plt.legend()
plt.show()







import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [[30,40,35,60,42],
     [45,67,30,40,60]]
plt.xlabel("Days",fontsize = 15)
plt.ylabel("Number of People",fontsize = 15)
plt.title("Data of a Restaurant",fontsize = 17)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x, y[0],color = "blue",width = 0.3, label = "men")
ax.bar(x, y[1],color = "pink",width = 0.3, label = "women")
#colors = ["magenta","hotpink"]
#plt.bar(x,y, color = colors,edgecolor ="black", linewidth = 2, linestyle = "-.",alpha = 0.5)
plt.show()



# import tkinter as tk
#
# window = tk.Tk()
#
# l = tk.Label(window, text = "not available")
# l.pack()
#
# def click():
#     if(var1.get()==1) & (var2.get()==0):
#         l.config(text = "it is the capital of India")
#     elif(var1.get()==0 & (var2.get()==1)):
#         l.config(text= "it is the capital of Maharashtra")
#
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
#
# cb = tk.Checkbutton(window, text = "New Delhi",variable= var1,onvalue=1, offvalue=0,command = click).pack()
# cb2 = tk.Checkbutton(window, text = "Mumbai",variable= var2,onvalue=1, offvalue=0,command = click).pack()
#
# window.mainloop()
#
