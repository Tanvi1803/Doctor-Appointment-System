# import tkinter as tk
# import subprocess
# import tkinter




# ####
# def execute_file():
#     subprocess.call(["python","index.py"])

# def service():
#     subprocess.call(["python","service.py"])   

# def cont():
#     subprocess.call(["python","contactpage.py"]) 

# def book():
#     subprocess.call(["python","book.py"]) 

# ###


# # Create a tkinter window
# root = tk.Tk()
# root.geometry("600x500")


# frame = tkinter.LabelFrame(root, text="Home Page")
# frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)




# Admin_login_button = tk.Button(frame, text="Admin_Login", command=execute_file)
# Admin_login_button.grid(row=0, column=1, padx=10, pady=10)



# services_button = tk.Button(frame, text="Services", command=service)
# services_button.grid(row=0, column=3, padx=10, pady=10)

# contact_us_button = tk.Button(frame, text="Contact_us", command=cont)
# contact_us_button.grid(row=0, column=4, padx=10, pady=10)



# book_appointment_button = tk.Button(root, text="Book_appointment", command=book)
# book_appointment_button.grid(row=2, column=2, columnspan=4, pady=20, sticky="nsew")

# # button.grid(row=0, column=0, sticky="nsew")




# root.mainloop()


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for handling images
import subprocess

# Functions to execute other scripts
def execute_file():
    subprocess.call(["python", "index.py"])

def service():
    subprocess.call(["python", "service.py"])

def cont():
    subprocess.call(["python", "contactpage.py"])

def book():
    subprocess.call(["python", "book.py"])

# Hover effect for buttons
def on_enter(e):
    e.widget["background"] = "#555555"
    e.widget["foreground"] = "#ffffff"

def on_leave(e):
    e.widget["background"] = e.widget.default_bg
    e.widget["foreground"] = e.widget.default_fg

# Create a tkinter window
root = tk.Tk()
root.title("Home Page")

# Set fullscreen mode
root.attributes("-fullscreen", True)

# Get screen dimensions for dynamic resizing
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load and set the background image
background_image = Image.open("images (6).jpeg")  # Replace 'images (6).jpeg' with your image file
background_image = background_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)  # Resize to fit the screen
bg_photo = ImageTk.PhotoImage(background_image)

# Create a Canvas widget to hold the background image
canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Title Label
title_label = tk.Label(canvas, text="Welcome to Our Application", font=("Helvetica", 30, "bold"), bg="#000000", fg="#ffffff")
canvas.create_window(screen_width // 2, 100, window=title_label)

# Create a frame for navigation buttons
frame = tk.LabelFrame(canvas, text="Navigation", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#555", padx=20, pady=20, borderwidth=2, relief="groove")
canvas.create_window(screen_width // 2, screen_height // 2 - 100, window=frame)

# Create a styled button function
def create_button(frame, text, command, bg, fg):
    button = tk.Button(frame, text=text, font=("Helvetica", 16), bg=bg, fg=fg, padx=20, pady=10, relief="flat", command=command)
    button.default_bg = bg
    button.default_fg = fg
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button

# Add buttons to the frame
admin_button = create_button(frame, "Admin Login", execute_file, "#4caf50", "white")
admin_button.grid(row=0, column=0, padx=20, pady=20)

services_button = create_button(frame, "Services", service, "#2196f3", "white")
services_button.grid(row=0, column=1, padx=20, pady=20)

contact_button = create_button(frame, "Contact Us", cont, "#ff9800", "white")
contact_button.grid(row=0, column=2, padx=20, pady=20)

# Book Appointment button
book_button = create_button(canvas, "Book Appointment", book, "#9c27b0", "white")
canvas.create_window(screen_width // 2, screen_height - 150, window=book_button)

# Footer label
footer_label = tk.Label(canvas, text="© 2025 Your Company Name", font=("Helvetica", 14), bg="#000000", fg="#ffffff", padx=10, pady=5)
canvas.create_window(screen_width // 2, screen_height - 50, window=footer_label)

# Exit on pressing the Escape key
root.bind("<Escape>", lambda e: root.destroy())

# Start the tkinter event loop
root.mainloop()



























































