# from tkinter import *
# root = Tk()
# root.title("First GUI")
# root.geometry("500x500")

# w = Label(root, text="Mentor International School\nPune-Maharashtra-India",font="aril 11 bold",bg="black",fg="white")
# w.pack(pady=5,padx=1)

# User_Name=Label(root,text="Student Name",font="aril 9 bold",bg="white",fg="red")
# UserNameInput=Entry(root)
# User_Name.pack(pady=5)
# UserNameInput.pack(pady=5)

# User_ROLL_Number=Label(root,text="Student Roll Number",font="aril 9 bold",bg="white",fg="red")
# UserRollNumber=Entry(root)
# User_ROLL_Number.pack(pady=5)
# UserRollNumber.pack(pady=5)

# button=Button(root, text="Close",font="aril 10 bold", width=18,command=root.destroy)
# button.pack()

# root.mainloop()
##====================================================================
########## Example "Entry"  ###########

from tkinter import *
from tkinter import ttk
Master=Tk()
Master.title("School Entry Book")
Master.geometry("900x500")

def DataDisplay():
    FirstName=Entry1.get()
    LastName=Entry2.get()
      
    # Retrieve the values of Checkbox
    SubjectSelection=[]
    if Marathi.get() == 1:
        SubjectSelection.append('Marathi')
    if Hindi.get() == 1:
        SubjectSelection.append('Hindi')
    if not SubjectSelection:
        SubjectSelection.append('Not Selected')
    
    # Join subjects if more than one is selected
    # SubjectSelection =",".join(SubjectSelection)

    # Retrieve the values of the RadioButoon
    GenderSelection='Male' if Gender.get() == 1 else 'Female'

    # Retrieve the values of the ListBox
    CourseModeSelection=[]
    Selected_Modes=LB.curselection()
    if Selected_Modes:
        for index in Selected_Modes:
            if index == 0:
                CourseModeSelection.append('Online')
            elif index == 1:
                CourseModeSelection.append('OFFline')
            elif index == 2:
                CourseModeSelection.append('Hybrid')
    else: 
        CourseModeSelection.append('Not Selected')    
    
    selected_Item=ComboBox.get()
    print(f"Selected:{selected_Item}")

      # Display the input data and selected gender
    Label(Master,text=f"First Name:{FirstName} \nLast Name:{LastName}\nGender:{GenderSelection}\nSubject:{SubjectSelection}\nMode:{CourseModeSelection}\n{selected_Item}").grid(row=10,column=0)
  
def Clearall():
    Entry1.delete(0,END)
    Entry2.delete(0,END)
    Gender.set(0)
    Marathi.set(0)
    Hindi.set(0)
    LB.selection_clear(0,END)
    ComboBox.set("") 
 

Label(Master,text="First Name").grid(row=0)
Label(Master,text="Last Name").grid(row=1)
Entry1=Entry(Master)
Entry2=Entry(Master)
Entry1.grid(row=0,column=1)
Entry2.grid(row=1,column=1)

## Radiobutton- example

Gender=IntVar()
Radiobutton(Master,text="MALE",variable=Gender,value=1).grid(row=4,column=0)
Radiobutton(Master,text="FEMALE",variable=Gender,value=2).grid(row=4,column=1)



## CheckBOX- example
Marathi = IntVar()
Hindi = IntVar()
Checkbutton(Master,text="Marathi",variable=Marathi).grid(row=5,column=0)
Checkbutton(Master,text="Hindi",variable=Hindi).grid(row=5,column=1)

## ListBox -Example
LB=Listbox(Master,selectmode=SINGLE)
LB.insert(1,"Online")
LB.insert(2,"Offline")
LB.insert(3,"Hybrid")
LB.grid(row=6,column=4)

##===================================
## MENU BAR - Example - 

# Create the menu bar
menu=Menu(Master)
Master.config(menu=menu)

# Create the File Menu
Filemenu=Menu(menu)
menu.add_cascade(label='File',menu=Filemenu)
Filemenu.add_command(label='New File')
Filemenu.add_command(label='Open File...',accelerator='CTRL+O') # Added accelerator
Filemenu.add_command(label="Save",accelerator='CTRL+S')
Filemenu.add_command(label="Save As...")
Filemenu.add_separator()

# Create the Help Menu
Helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=Helpmenu)
Helpmenu.add_command(label='About')

# Add the Exit command
Filemenu.add_command(label='Exit', command=Master.quit)


# Define the function to handle the ComboBox Event
def ON_Select(event):
    selected_Item=ComboBox.get()
    print(f"Selected:{selected_Item}")

# Create a Combobox
ComboBox=ttk.Combobox(Master,values=["Option-1","Option-2","Option-3"])
ComboBox.grid(row=5,column=6)
# Set default value
ComboBox.set("Option-1")
# Bind event to selection
ComboBox.bind("<<ComboboxSelected>>",ON_Select)





##========================================,
SubmiteButton=Button(Master,text="Submit",command=DataDisplay)
SubmiteButton.grid(row=24,column=1)

ClearButton=Button(Master,text="Clear All",command=Clearall)
ClearButton.grid(row=26,column=1)

CloseButton=Button(Master,text="Close Form",command=Master.destroy)
CloseButton.grid(row=28,column=1)

mainloop()
#### ==============================

