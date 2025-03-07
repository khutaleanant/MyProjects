from tkinter import*

Master=Tk()
Master.title("SPINBOX")
Master.geometry("400x400")
w=Spinbox(Master, from_=-20,to=20)
w.pack(pady=10)
mainloop()