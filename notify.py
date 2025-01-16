from tkinter import *
import tkinter as tk
import sqlite3

root = Tk()
root.geometry('600x500')
root.title("Requested appointments")

frame = tk.Frame(root)
frame.pack()
def next():
    nx=Tk()
    nx.geometry("500x650")
    nx.maxsize(500, 650)
    nx.minsize(500, 650)
    nx.title("Requested Appointments")
    label = Label(frame, text="Requested Appointments", font="time 25 bold",bg = 'blue', fg = 'white')
    label.grid(row=0, column=0, columnspan=20)
    pl = Label(frame, text="Name", font="time 15 bold")
    pl.grid(row=1, column=0, padx=10, pady=10)

    p6 = Label(frame, text="Age", font="time 15 bold")
    p6.grid(row=1, column=1, padx=10, pady=10)

    p2 = Label(nx, text="Email", font="time 15 bold")
    p2.grid(row=1, column=2, padx=10, pady=10)

    p3 = Label(nx, text="Gender", font= "time 15 bold")
    p3.grid(row=1, column=3, padx=10, pady=10)

    p4 = Label(nx, text="Doctor", font= "time 15 bold")
    p4.grid(row=1, column=4, padx=10, pady=10)

    p5 = Label(nx, text="Contactno", font= "time 15 bold")
    p5.grid(row=1, column =5, padx = 10, pady = 10)



    # my_conn = sqlite3.connect()
    # my_conn.execute("SELECT * FROM student limit 0,10")
    conn = sqlite3.connect('Form.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute("select * from student")
        r = cursor.fetchall()

        num = 2
        for i in r:
              name = Label(frame, text= i[0] , font ="time 12 bold", fg = "blue")
              name.grid(row=num, column=0, padx=10, pady=10)

              age = Label(frame, text=i[1], font="time 12 bold", fg="blue")
              age.grid(row=num, column=1, padx=10, pady=10)

              email = Label(nx, text=i[2], font="time 12 bold", fg="blue")
              email.grid(row=num, column=2, padx=10, pady=10)

              gender = Label(nx, text=i[3], font="time 12 bold", fg="blue")
              gender.grid(row=num, column=3, padx=10, pady=10)

              doc = Label(nx, text=i[4], font="time 12 bold", fg="blue")
              doc.grid(row=num, column=4, padx=10, pady=10)

              cont = Label(nx, text=i[5], font="time 12 bold", fg="blue")
              cont.grid(row=num, column=5, padx=10, pady=10)
              num = num + 1

    conn.commit()
    conn.close()

root.mainloop()