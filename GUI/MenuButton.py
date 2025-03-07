from tkinter import*
Master=Tk()
Master.title("MENU BUTTON PRACTICE")
MB=Menubutton(Master,text="File")
MB.grid(row=1,column=1)
MB.menu=Menu(MB,tearoff=0)
MB["menu"]=MB.menu
cVar = IntVar()
aVar = IntVar()
MB.menu.add_checkbutton(label="Contact",variable=cVar)
MB.menu.add_checkbutton(label="About",variable=aVar)

Master.mainloop()