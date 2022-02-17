from tkinter import *

def calculate():
    """converts miles to kilometres"""
    kilomtetres = int(km.get())
    kilomtetres *= 1.60934
    label_4.config(text=kilomtetres)

# set up the screen environment
window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

# set up the labels
my_label = Label(text="Miles", font=("Arial", 12, "bold"))
my_label.grid(column=3, row= 1)
my_label.config(padx=10, pady=10)

label_2 = Label(text="KM", font=("Arial", 12, "bold"))
label_2.grid(column=3, row=2)
label_2.config(padx=10, pady=10)

label_3 = Label(text="is equal to", font=("Arial", 12, "bold"))
label_3.grid(column=1, row= 2)
label_3.config(padx=5, pady=5)

label_4 = Label(text=0, font=("Arial", 12, "bold"))
label_4.grid(column=2, row= 2)
label_4.config(padx=10, pady=10)

# entry
km = Entry(width=10)
km.grid(column=2, row=1)

# design button
new_button = Button(text="Calulate", command=calculate)
new_button.grid(column=2, row=3)

window.mainloop()
