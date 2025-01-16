# from tkinter import *
# import sqlite3
# import subprocess

# root = Tk()
# root.geometry('600x500')
# root.title("Appointment")

# def execute_file():
#     # Call the other Python file using subprocess
#     subprocess.call(["python", "docoptions.py"])

# Fullname = StringVar()
# age= IntVar()
# Email = StringVar()
# var = IntVar()
# c = StringVar()
# contactno = IntVar()


# def database():
#     name1 = Fullname.get()
#     age1 = age.get()
#     email = Email.get()
#     gender = var.get()
#     country = c.get()
#     cont = contactno.get()
#     conn = sqlite3.connect('Form.db')

#     with conn:
#         cursor = conn.cursor()
#     cursor.execute(
#         'CREATE TABLE IF NOT EXISTS "Student" ( "Fullname" TEXT, "Email" TEXT, "Gender" TEXT, "Country" TEXT, "contact" TEXT, "age" Int )')
#     cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,contact,age) VALUES(?,?,?,?,?,?)',
#                    (name1, email, gender, country, cont,age1))
#     conn.commit()
#     cursor.close()


# label_0 = Label(root, text="Book an Appointment", width=20, font=("bold", 20))
# label_0.place(x=90, y=53)

# label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
# label_1.place(x=80, y=130)

# entry_1 = Entry(root, textvar=Fullname)
# entry_1.place(x=240, y=130)

# label_12 = Label(root, text="Age", width=20, font=("bold", 10))
# label_12.place(x=68, y=170)
# entry_12 = Entry(root, textvar=age)
# entry_12.place(x=240, y=170)

# label_2 = Label(root, text="Email", width=20, font=("bold", 10))
# label_2.place(x=68, y=200)

# entry_2 = Entry(root, textvar=Email)
# entry_2.place(x=240, y=200)

# label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
# label_3.place(x=70, y=230)

# Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
# Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

# label_4 = Label(root, text="Doctor", width=20, font=("bold", 10))
# label_4.place(x=70, y=280)

# list1 = ['Dr.Kapoor', 'Dr.Raje', 'Dr.Vaje', 'Dr.Somnath', 'Dr.Patil', 'Dr.Pawar'];

# Button(root, text='Search', width=30, bg='black', fg='white', command=execute_file).place(x=300, y=280)

# droplist = OptionMenu(root, c, *list1)
# droplist.config(width=15)
# c.set('select doctor')
# droplist.place(x=240, y=280)

# # label_4 = Label(root, text="Programming", width=20, font=("bold", 10))
# # label_4.place(x=85, y=330)
# # var2 = IntVar()
# # Checkbutton(root, text="java", variable=var1).place(x=235, y=330)
# #
# # Checkbutton(root, text="python", variable=var2).place(x=290, y=330)
# label_4 = Label(root, text="Contactno", width=20, font=("bold", 10))
# label_4.place(x=85, y=330)

# entry_4 = Entry(root, textvar=contactno)
# entry_4.place(x=235, y=330)


# Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

# root.mainloop()

from tkinter import *
import sqlite3
import subprocess

# Create the main window
root = Tk()
root.geometry('800x600')  # Increased size for better layout
root.title("Appointment Booking")

# Variables
Fullname = StringVar()
age = IntVar()
Email = StringVar()
var = IntVar()
c = StringVar()  # Variable to hold the selected doctor
contactno = IntVar()

# Function to execute the doctor search file
def execute_file():
    # Call the other Python file using subprocess
    subprocess.call(["python", "docoptions.py"])
    # After the docoptions.py script completes, you can manually update the selected doctor.
    # For now, we'll set an example doctor for demonstration purposes.
    c.set("Dr. Kapoor")  # Replace with the actual doctor selection logic.

# Database Function
def database():
    name1 = Fullname.get()
    age1 = age.get()
    email = Email.get()
    gender = "Male" if var.get() == 1 else "Female"
    doctor = c.get()
    cont = contactno.get()
    conn = sqlite3.connect('Form.db')

    with conn:
        cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS "Student" 
        ("Fullname" TEXT, "Email" TEXT, "Gender" TEXT, "Doctor" TEXT, "Contact" TEXT, "Age" INT)'''
    )
    cursor.execute(
        'INSERT INTO Student (FullName, Email, Gender, Doctor, Contact, Age) VALUES (?, ?, ?, ?, ?, ?)',
        (name1, email, gender, doctor, cont, age1),
    )
    conn.commit()
    cursor.close()

# Title Label
label_0 = Label(
    root, 
    text="Book an Appointment", 
    width=30, 
    font=("Helvetica", 24, "bold"), 
    bg="blue", 
    fg="white", 
    pady=10
)
label_0.pack(pady=20)

# Form Fields
form_frame = Frame(root, padx=20, pady=20)
form_frame.pack()

# Full Name
label_1 = Label(form_frame, text="Full Name", font=("Helvetica", 12, "bold"))
label_1.grid(row=0, column=0, pady=10, sticky=E)
entry_1 = Entry(form_frame, textvar=Fullname, font=("Helvetica", 12), width=30)
entry_1.grid(row=0, column=1, pady=10, padx=10)

# Age
label_12 = Label(form_frame, text="Age", font=("Helvetica", 12, "bold"))
label_12.grid(row=1, column=0, pady=10, sticky=E)
entry_12 = Entry(form_frame, textvar=age, font=("Helvetica", 12), width=30)
entry_12.grid(row=1, column=1, pady=10, padx=10)

# Email
label_2 = Label(form_frame, text="Email", font=("Helvetica", 12, "bold"))
label_2.grid(row=2, column=0, pady=10, sticky=E)
entry_2 = Entry(form_frame, textvar=Email, font=("Helvetica", 12), width=30)
entry_2.grid(row=2, column=1, pady=10, padx=10)

# Gender
label_3 = Label(form_frame, text="Gender", font=("Helvetica", 12, "bold"))
label_3.grid(row=3, column=0, pady=10, sticky=E)
gender_frame = Frame(form_frame)
gender_frame.grid(row=3, column=1, pady=10, sticky=W)
Radiobutton(gender_frame, text="Male", padx=5, variable=var, value=1, font=("Helvetica", 12)).pack(side=LEFT)
Radiobutton(gender_frame, text="Female", padx=20, variable=var, value=2, font=("Helvetica", 12)).pack(side=LEFT)

# Doctor
label_4 = Label(form_frame, text="Doctor", font=("Helvetica", 12, "bold"))
label_4.grid(row=4, column=0, pady=10, sticky=E)

doctor_frame = Frame(form_frame)
doctor_frame.grid(row=4, column=1, pady=10, sticky=W)

# Initial button to open doctor search
search_button = Button(
    doctor_frame, 
    text='Search Doctor', 
    width=20, 
    bg='green', 
    fg='white', 
    font=("Helvetica", 12), 
    command=execute_file
)
search_button.pack(side=LEFT)

# Dropdown to show selected doctor
droplist = OptionMenu(doctor_frame, c, *['Dr. Kapoor', 'Dr. Raje', 'Dr. Vaje', 'Dr. Somnath', 'Dr. Patil', 'Dr. Pawar'])
droplist.config(font=("Helvetica", 12), width=15)
c.set('Select Doctor')  # Default text before selection
droplist.pack(side=LEFT, padx=10)

# Contact Number
label_5 = Label(form_frame, text="Contact Number", font=("Helvetica", 12, "bold"))
label_5.grid(row=5, column=0, pady=10, sticky=E)
entry_5 = Entry(form_frame, textvar=contactno, font=("Helvetica", 12), width=30)
entry_5.grid(row=5, column=1, pady=10, padx=10)

# Buttons
button_frame = Frame(root, pady=20)
button_frame.pack()

Button(
    button_frame, text='Submit', width=20, bg='blue', fg='white', 
    font=("Helvetica", 12), command=database
).grid(row=0, column=0, padx=10)

Button(
    button_frame, text='Exit', width=20, bg='red', fg='white', 
    font=("Helvetica", 12), command=root.destroy
).grid(row=0, column=1, padx=10)

# Run the main loop
root.mainloop()
