# from tkinter import*
# Master=Tk()
# Master.title("Panned Window Practice")
# M1=PanedWindow()
# M1.pack(fill=BOTH,expand=1)
# left=Entry(M1,bd=5)
# M1.add(left)

# M2=PanedWindow(M1,orient=VERTICAL)
# M1.add(M2)
# top=Scale(M2,orient=HORIZONTAL)
# M2.add(top)
# mainloop()
##====================================
from tkinter import *


# Create the main window
Master = Tk()
Master.title("Panned Window Practice")

# Create the first PanedWindow
M1 = PanedWindow(Master)
M1.pack(fill=BOTH, expand=1)

# Add an entry widget to the left side of the first paned window
left = Entry(M1, bd=5)
M1.add(left)

# Create the second PanedWindow with a vertical orientation
M2 = PanedWindow(M1, orient=VERTICAL)
M1.add(M2)

# Add a horizontal scale widget inside the second PanedWindow
top = Scale(M2, orient=HORIZONTAL)
M2.add(top)

# Start the main event loop
mainloop()


