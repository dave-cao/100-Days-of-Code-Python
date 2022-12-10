# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import json
import random
import tkinter as tk
from tkinter import messagebox

import pyperclip


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    website_input.delete(0, len(website))
    username = username_input.get()
    username_input.delete(0, len(username))
    password = password_input.get()
    password_input.delete(0, len(password))

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if not len(website) or not len(username) or not len(password):
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        try:
            with open("data.json", "r") as file:
                # Load and update json file
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                # rewrite all json file
                json.dump(data, file, indent=4)


def search_websites():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

            website_data = data[website_input.get()]
            messagebox.showinfo(
                message=f"Email: {website_data['email']}\n Password: {website_data['password']}"
            )
    except KeyError:
        messagebox.showwarning(message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showwarning(message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"
FONT_SIZE = 15

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_image = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Website
website_label = tk.Label(
    text="Website: ", font=(FONT_NAME, FONT_SIZE), highlightthickness=0
)
website_label.grid(column=0, row=1)
website_input = tk.Entry(width=20, highlightthickness=0)
website_input.grid(column=1, row=1)
website_input.focus()

# Email Username
username_label = tk.Label(
    text="Email/Username", font=(FONT_NAME, FONT_SIZE), highlightthickness=0
)
username_label.grid(column=0, row=2)
username_input = tk.Entry(width=35, highlightthickness=0)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "davidcaohoang@yahoo.ca")

# Password
password_label = tk.Label(
    text="Password", font=(FONT_NAME, FONT_SIZE), highlightthickness=0
)
password_label.grid(column=0, row=3)
password_input = tk.Entry(width=16, highlightthickness=0)
password_input.grid(column=1, row=3)

# Buttons
generate_pass = tk.Button(
    text="Generate Password", highlightthickness=0, command=generate_password
)
generate_pass.grid(column=2, row=3)
add_button = tk.Button(
    text="Add", width=33, highlightthickness=0, command=save_password
)
add_button.grid(column=1, row=4, columnspan=2)

# search
search_button = tk.Button(text="Search", highlightthickness=0, command=search_websites)
search_button.grid(column=2, row=1)

window.mainloop()
