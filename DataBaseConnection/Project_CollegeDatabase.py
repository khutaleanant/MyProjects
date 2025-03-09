import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anant@1080", # Change as per your MySQL credentials
        )

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = course_var.get()
    contact = entry_contact.get()
    
    if not (name and age and gender and course and contact):
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                gender VARCHAR(10),
                course VARCHAR(50),
                contact VARCHAR(15)
            )
        """)
        
        cursor.execute("""
            INSERT INTO students (name, age, gender, course, contact)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, age, gender, course, contact))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Student details saved successfully!")
        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error: {str(e)}")

def clear_form():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    gender_var.set("None")
    course_var.set("Select Course")

# Creating main window
root = tk.Tk()
root.title("College Student Entry Form")
root.geometry("400x350")

# Labels and Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

# Gender Selection
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=1, sticky="w")

# Course Selection
tk.Label(root, text="Course:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
course_var = tk.StringVar(value="Select Course")
courses = ["Computer Science", "Electronics", "Mechanical", "Civil"]
course_dropdown = tk.OptionMenu(root, course_var, *courses)
course_dropdown.grid(row=4, column=1, padx=10, pady=5)

# Contact Number
tk.Label(root, text="Contact:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_contact = tk.Entry(root)
entry_contact.grid(row=5, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Submit", command=submit_form).grid(row=6, column=0, padx=10, pady=20)
tk.Button(root, text="Clear", command=clear_form).grid(row=6, column=1, padx=10, pady=20)

root.mainloop()