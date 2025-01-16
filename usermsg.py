from tkinter import *
import tkinter as tk
import sqlite3


root = Tk()
root.geometry('800x600')
root.title("Requested appointments")

frame = tk.Frame(root)
frame.pack()

user_frame = tk.LabelFrame(frame, text="User Information")
user_frame.grid(row=0, column=0, padx=20, pady=10)

label = Label(user_frame , text="Requested Appointments", font="time 25 bold",bg = 'blue', fg = 'white')
label.grid(row=0, column=0, columnspan=20)
pl = Label(user_frame , text="Name", font="time 15 bold")
pl.grid(row=1, column=0, padx=10, pady=10)

p6 = Label(user_frame , text="Age", font="time 15 bold")
p6.grid(row=1, column=1, padx=10, pady=10)

p2 = Label(user_frame , text="Email", font="time 15 bold")
p2.grid(row=1, column=2, padx=10, pady=10)

p3 = Label(user_frame , text="Gender", font= "time 15 bold")
p3.grid(row=1, column=3, padx=10, pady=10)

p4 = Label(user_frame , text="Doctor", font= "time 15 bold")
p4.grid(row=1, column=4, padx=10, pady=10)

p5 = Label(user_frame , text="Contactno", font= "time 15 bold")
p5.grid(row=1, column =5, padx = 10, pady = 10)

p7 = Label(user_frame , text="Requests", font= "time 15 bold")
p7.grid(row=1, column =6, padx = 10, pady = 10)


conn = sqlite3.connect('Form.db')
with conn:
        cursor = conn.cursor()
        cursor.execute("Insert into student1 select * from student")

root.mainloop()