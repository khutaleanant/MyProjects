from tkinter import*
Master=Tk()
Master.title("TEXT BOX")
Label(Master,text="Your Comments").pack()
T=Text(Master,height=2,width=30)
T.pack(pady=20)
T.insert(END,"BEST WEB SITE\nALL THE BEST !!")
mainloop()