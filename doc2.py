import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Doctor Info")
window.geometry('600x500')
frame = tk.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="Doctor Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

Doc_frame = tk.LabelFrame(frame, text="Doctor Information")
Doc_frame.grid(row=0, column=0, padx=20, pady=10)

image1 = Image.open("doc.jpg")
image1 = image1.resize((200, 200), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(Doc_frame , image=photo1)
label1.pack()

name_label = tk.Label(Doc_frame, text="Name: Dr. Rajeev Kapoor")
name_label.pack()

name_label = tk.Label(Doc_frame, text="Education: Md")
name_label.pack()

name_label = tk.Label(Doc_frame, text="Specialization: Dermatologist")
name_label.pack()

name_label = tk.Label(Doc_frame, text="Years of Experience:25")
name_label.pack()

Doc1_frame = tk.LabelFrame(frame, text="Doctor Information")
Doc1_frame.grid(row=0, column=1, padx=20, pady=10)

image2 = Image.open("doc2.jpg")
image2 = image2.resize((200, 200), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(Doc1_frame  , image=photo2)
label2.pack()

name_label1 = tk.Label(Doc1_frame , text="Name: Dr. Patil")
name_label1.pack()

name_label2 = tk.Label(Doc1_frame , text="Education: BDS")
name_label2.pack()

name_label3 = tk.Label(Doc1_frame , text="Specialization: Dermatologist")
name_label3.pack()

name_label4 = tk.Label(Doc1_frame , text="Years of Experience:20")
name_label4.pack()





window.mainloop()