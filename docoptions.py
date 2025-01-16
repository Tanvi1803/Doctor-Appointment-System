import tkinter as tk
import subprocess
import tkinter

# Create a function to execute when the login button is clicked


####
def derma():
    subprocess.call(["python","doc2.py"])

def den():
    subprocess.call(["python","service.py"])   

def ortho():
    subprocess.call(["python","contactpage.py"]) 

def pedia():
    subprocess.call(["python","book.py"]) 

def psyc():
    subprocess.call(["python","book.py"])     

###


# Create a tkinter window
root = tk.Tk()
root.geometry("600x500")


frame = tkinter.LabelFrame(root, text="Specialization")
frame.grid(row=2, column=0, sticky="news", padx=150, pady=150)

# Create a login button and add it to the window


derma_button = tk.Button(frame, text="Dermatologists", command=derma)
derma_button.grid(row=0, column=1, padx=10, pady=10)

den_button = tk.Button(frame, text="Dentists", command=den)
den_button.grid(row=0, column=2, padx=10, pady=10)

ortho_button = tk.Button(frame, text="Orthopedics", command=ortho)
ortho_button.grid(row=0, column=3, padx=10, pady=10)

pedia_button = tk.Button(frame, text="Pediatrics", command=pedia)
pedia_button.grid(row=1, column=1, padx=10, pady=10)

psyc_button = tk.Button(frame, text="Pediatrics", command=psyc)
psyc_button.grid(row=1, column=2, padx=10, pady=10)




root.mainloop()

####
# def Contact_us():
#     print("Contact_us button clicked")
    
# ###

# ###   
# def Book_appointment():
#     print("Book_appointment button clicked")


# # Create a tkinter window
# root = tk.Tk()
# root.geometry("500x300")
# # Create a login button and add it to the window
# # Create a login button and add it to the window
# Admin_login_button = tk.Button(root, text="Admin_Login", command=execute_file)
# Admin_login_button.grid(row=0, column=0, padx=(10, 5), pady=10)

# User_login_button = tk.Button(root, text="User_Login", command=User_login)
# User_login_button.grid(row=0, column=1, padx=5, pady=10)

# services_button = tk.Button(root, text="Services", command=Services)
# services_button.grid(row=0, column=2, padx=5, pady=10)

# contact_us_button = tk.Button(root, text="Contact_us", command=Contact_us)
# contact_us_button.grid(row=0, column=3, padx=5, pady=10)

# book_appointment_button = tk.Button(root, text="Book_appointment", command=Book_appointment)
# book_appointment_button.grid(row=1, column=0, columnspan=4, pady=20)


# # Start the tkinter event loop
# root.mainloop()
