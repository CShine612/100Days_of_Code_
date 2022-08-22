from tkinter import *
from tkinter import messagebox
import json
import random, pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
                    [random.choice(symbols) for _ in range(random.randint(2, 4))] + \
                    [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(END, password)
    pyperclip.copy(pass_input.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_input.get()
    user = user_input.get()
    password = pass_input.get()
    new_data = {website: {"email": user, "password": password}}

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Some fields left blank")
    else:
        messagebox.askokcancel(title=website, message=f"There are the details you entered: \nEmail: {user} "
                                                      f"\nPassword: {password} \nWould you like to save these details?")
        try:
            with open("data.json", "r") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            data = {}
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        website_input.delete(0, END)
        pass_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def pass_search():
    site = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        try:
            credentials = data[site]
        except KeyError:
            messagebox.showerror(title="Error", message="No site by that name was found")
        else:
            user = credentials["email"]
            password = credentials["password"]
            messagebox.showinfo(title=f"{site}", message=f"Email: {user}\n Password: {password}")
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=22)
website_input.grid(column=1, row=1, sticky="EW")

user_input = Entry(width=40)
user_input.grid(column=1, row=2, columnspan=2, sticky="EW")
user_input.insert(END, "cshine612@gmail.com")

pass_input = Entry(width=22)
pass_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=5, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=pass_search)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
