import tkinter as tk

# create a window
window = tk.Tk()

# create a label to display fetched data
label1 = tk.Label(window, text="Data will be fetched")

# define a function to fetch data and update the label
def fetch_data():
    # fetch data from a source
    data = "Accepted"
    # update the label with the fetched data
    label1.config(text=data)
    # create a button after data is fetched
    label2 = tk.Label(window, text="Accepted")
    label2.pack()

# create a button to fetch data
fetch_button = tk.Button(window, text="Accept", command=fetch_data)
fetch_button.pack()

# display the label and start the main loop
label1.pack()
window.mainloop()