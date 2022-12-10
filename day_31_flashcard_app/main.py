import random
import tkinter as tk

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

# Variables
title = "Title"
word = "Word"

# ============================== CSV ======================================
try:
    data = pandas.read_csv("./data/words_to_learn.csv").iterrows()
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv").iterrows()

word_dict = [{"French": row.French, "English": row.English} for (_, row) in data]


def flip_card():
    global flip_timer, pair_object
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_front, image=card_front_img)
    pair_object = random.choice(word_dict)
    french_word = pair_object["French"]
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(title_text, text="French", fill="black")
    flip_timer = window.after(3000, delay)


def clicked_y():
    try:
        word_dict.remove(pair_object)
        new_word_dict = pandas.DataFrame(word_dict)
        new_word_dict.to_csv("./data/words_to_learn.csv")
        flip_card()
    except NameError:
        # If beginning of game
        flip_card()


def delay():
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=pair_object["English"], fill="white")


def empty():
    pass


# ============================== UI =========================================

# Configure windows
window = tk.Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)


flip_timer = window.after(3000, empty)
# Images
card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="./images/card_back.png")
x_button_img = tk.PhotoImage(file="./images/wrong.png")
y_button_img = tk.PhotoImage(file="./images/right.png")

# Manipulate canvas
canvas = tk.Canvas(width=815, height=540, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = canvas.create_image(404, 270, image=card_front_img)
title_text = canvas.create_text(404, 180, text=title, font=(FONT_NAME, 20, "italic"))
word_text = canvas.create_text(404, 270, text=word, font=(FONT_NAME, 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons with images
x_button = tk.Button(
    image=x_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card
)
y_button = tk.Button(
    image=y_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=clicked_y
)
x_button.grid(column=0, row=1)
y_button.grid(column=1, row=1)


window.mainloop()
