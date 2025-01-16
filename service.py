import tkinter as tk
from tkinter import *
root = Tk()

# Create a new window for services information
services_window = tk.Toplevel(root)
services_window.title("Our Services")
services_window.geometry("600x400")

# Create a label to display services information
services_label = tk.Label(services_window, text="We offer a wide range of medical services including:\n\n- General checkups\n- Vaccinations\n- Emergency care\n- Surgery\n- Pediatrics\n- Cardiology\n- Dermatology\n- Neurology\n- Gastroenterology\n- And more!", font=("Arial", 14))
services_label.pack()

root.mainloop()