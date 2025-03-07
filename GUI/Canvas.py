from tkinter import*
Master=Tk()
Master.title("First Canvas")
CANVA=Canvas(Master,width=50,height=50)
CANVA.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
CANVA.create_line(0,y,canvas_width,y)
mainloop()