import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sqlite3
from tkinter import StringVar, IntVar
#import openpyxl


fname= StringVar()
lname=StringVar()
email=StringVar()
gender =StringVar()
doc=StringVar()
age= IntVar()

def database():
   global conn, cursor
   fname=fname.get()
   lname=lname.get()
   email=email.get()
   gender=gender.get()
   doc=doc.get()
   age=age.get()
   conn = sqlite3.connect('appointment.db')
   with conn:
        cursor=conn.cursor()
   cursor.execute('CREATE TABLE "user" ( "firstname " varchar(255) NOT NULL, "lastname" varchar(255) NOT NULL, "Age" INTEGER NOT NULL, "doc" varchar(200) NOT NULL, "email" TEXT , "gender" varchar(200))')
   cursor.execute('INSERT INTO user (firstname,lastname,Age,doc,email,gender) VALUES(?,?,?,?,?,?)',(fname,lname,age,doc,email,gender))
   conn.commit()


class EmailEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(validate='key')
        self.configure(validatecommand=(self.register(self._validate), '%P'))

    def _validate(self, value):
        pattern = r'^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$'
        if re.match(pattern, value):
            return True
        else:
            print("Invalid Email")
            self.bell()
            return False

def execute_file():
    # Call the other Python file using subprocess
    subprocess.call(["python", "doc2.py"])

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()


            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            
            print("------------------------------------------")


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame, textvariable=fname)
last_name_entry = tkinter.Entry(user_info_frame, textvar=lname)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."], textvar=gender)
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=110, intvar=age)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Select Doctor")
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Dr.Somnath", "Dr.Raje", "Dr.Vaje", "Europe", "North America", "Oceania",
                                            "South America"],textvar=doc)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

search_button = tkinter.Button(user_info_frame, text="     Search      ", command=execute_file)
search_button.grid(row=3, column=2)

email_label = tkinter.Label(user_info_frame, text="Email")
email_label.grid(row=4, column=0)
email_entry = EmailEntry(user_info_frame,textvar=email)
email_entry.grid(row=4, column=1)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

Button1=tk.Button(window, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
window.mainloop()
