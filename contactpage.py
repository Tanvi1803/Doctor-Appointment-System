import tkinter as tk
from tkinter import *
root = Tk()

# Create a new window for services information
services_window = tk.Toplevel(root)
services_window.title("Our Contact_us")
services_window.geometry("600x400")

# Create a label to display services information
services_label = tk.Label(services_window, text="WE OFFER OUR CONTACT_US AND EMAIL_ID:\n\n- Contact_number:9004335718\n- Email_id:rajitkapur123@gmail.com", font=("Arial", 14))
services_label.pack()

root.mainloop()