from tkinter import *

Master=Tk()
scollbar=Scrollbar(Master)
scollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(Master,yscrollcommand=scollbar.set)

for line in range(100):
    mylist.insert(END,"This is line number "+str(line))

mylist.pack(side=LEFT,fill=BOTH)
scollbar.config(command=mylist.yview)
mainloop()