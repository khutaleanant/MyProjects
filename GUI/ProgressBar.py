from tkinter import*
from tkinter import ttk
import time


# Create Function to command startbutton

def Start_Progress():
    progress.start()

    #Simulate a task that takes time to complete
    for i in range(101):
        #Simulated some work
        time.sleep(0.07)
        progress["value"]=i
        # ProgressLabel(MainFrame,text=i).pack()
        progress_label.config(text=f"Progress:{i}%")  # Update the label text
      
        #Update the GUI
        MainFrame.update_idletasks()
    progress.stop()    

#Create a progressbar widget

MainFrame=Tk()
MainFrame.title("Progress Bar")
MainFrame.geometry("600x600")
progress=ttk.Progressbar(MainFrame,length=100,orient=HORIZONTAL,mode="determinate")
progress.pack(pady=20)

# Create a label to display progress percentage
progress_label = Label(MainFrame, text="Progress: 0%")
progress_label.pack(pady=10)

#Create a Button "START"

StartButoon=ttk.Button(MainFrame,text="START PROGRESS",command=Start_Progress)
StartButoon.pack(pady=20)
mainloop()