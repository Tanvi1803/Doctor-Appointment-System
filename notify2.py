from tkinter import *
import tkinter as tk
import sqlite3




root = Tk()
root.geometry('1000x600')
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

label1 = Label(user_frame , text="Accept", font= "time 15 bold")
label1.grid(row=2, column =6, padx = 10, pady = 10)




def fetch_data():
    # fetch data from a source
    data = "Accepted"
    # update the label with the fetched data
    label1.config(text=data)
    # create a button after data is fetched



fetch_button = tk.Button(user_frame, text="Accept", command=fetch_data)
fetch_button.grid(row=2, column =7, padx = 10, pady = 10)


conn = sqlite3.connect('Form.db')
with conn:
        cursor = conn.cursor()
        cursor.execute("select * from student")
        r = cursor.fetchall()

        num = 2
        for i in r:
              name = Label(user_frame, text= i[0] , font ="time 12 bold", fg = "black")
              name.grid(row=num, column=0, padx=10, pady=10)

              age = Label(user_frame, text=i[1], font="time 12 bold", fg="black")
              age.grid(row=num, column=1, padx=10, pady=10)

              email = Label(user_frame, text=i[2], font="time 12 bold", fg="black")
              email.grid(row=num, column=2, padx=10, pady=10)

              gender = Label(user_frame, text=i[3], font="time 12 bold", fg="black")
              gender.grid(row=num, column=3, padx=10, pady=10)

              doc = Label(user_frame, text=i[4], font="time 12 bold", fg="black")
              doc.grid(row=num, column=4, padx=10, pady=10)

              cont = Label(user_frame, text=i[5], font="time 12 bold", fg="black")
              cont.grid(row=num, column=5, padx=10, pady=10)


              num = num + 1


conn.commit()
conn.close()

root.mainloop()
