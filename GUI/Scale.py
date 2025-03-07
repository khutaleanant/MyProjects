from tkinter import *
Master=Tk()
Master.title("SCALE PRACTICE")
Master.geometry("200x200")

Label(Master,text="SCALE Vartical").pack()
VerticalScale=Scale(Master,from_=0,to=50).pack()

Label(Master,text="SCALE Horizontal").pack()
HorizontalScale=Scale(Master,from_=0,to=50,orient=HORIZONTAL).pack()

mainloop()