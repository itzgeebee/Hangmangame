# A password manager that generates safe passwords when needed and stores login details on a local file
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

# set up your screen environment
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# set up the canvas environment
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="password_manager_updated\logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)


def pass_gen():
    """generates random safe passwords when called. automatically copies password in the clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password_generated = "".join(password_list)

    password.insert(0, password_generated)
    pyperclip.copy(password_generated)


def save_files():
    """ saves the user details into a local .txt file.Resets the entry fields to blank"""
    new_data = {
        website.get(): {
            "email": email_username.get(),
            "password": password.get()
        }

    }
    if website.get() == "" or email_username.get() == "" or password.get() == "":
        messagebox.showwarning(title="empty field", message="Please make sure all fields are filled")

    else:
        try:
            with open("password_manager.json", "r") as pm_file:
                # read old data
                dat = json.load(pm_file)
        except FileNotFoundError:
            with open("password_manager.json", "w") as pm_file:
                json.dump(new_data, pm_file, indent=4)
        else:
            # update old data with new data
            dat.update(new_data)
            with open("password_manager.json", "w") as pm_file:
                # saving updated data
                json.dump(dat, pm_file, indent=4)
        finally:
            website.delete(0, END)
            email_username.delete(0, END)
            password.delete(0, END)
            website.focus()
            email_username.insert(0, "balogungideon12@gmail.com")


def find_password():
    """checks the database for the login details of the specified website """
    webs = website.get()
    try:
        with open("password_manager.json", "r") as pm_file:
            tmp = json.load(pm_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No record found")
    else:
        if webs in tmp:
            messagebox.showinfo(title="login details \n ",
                                message=f"email: {tmp[webs]['email']} \n password: {tmp[webs]['password']} ")
            pyperclip.copy(tmp[webs]["password"])
        else:
            messagebox.showinfo(title="error", message="No record found")


# set up labels
website_label = Label(text="website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# set up the input
website = Entry(width=36)
website.grid(row=1, column=1, )
website.focus()

email_username = Entry(width=54)
email_username.grid(row=2, column=1, columnspan=2)
email_username.insert(0, "balogungideon12@gmail.com")

password = Entry(width=36)
password.grid(row=3, column=1)

# set up the buttons
generate_password = Button(text="Generate Password", command=pass_gen)
generate_password.grid(row=3, column=2, columnspan=2)

add_password = Button(text="Add", command=save_files)
add_password.config(width=31)
add_password.grid(row=4, column=1, )

search = Button(text="Search", command=find_password)
search.config(width=13)
search.grid(row=1, column=2, )

window.mainloop()
