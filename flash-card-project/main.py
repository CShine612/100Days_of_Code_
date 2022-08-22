from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"
LANGUAGE = "german"
TRANSLATE = "english"
FONT = "Arial"


# ---------------------------- Get DATA from CSV ------------------------------- #

try:
    data = pandas.read_csv(f"data/{LANGUAGE}_words_to_learn.csv")
    data_dict = {row[1][f"{LANGUAGE}"]: row[1][f"{TRANSLATE}"] for row in data.iterrows()}
except FileNotFoundError:
    data = pandas.read_csv(f"data/{LANGUAGE}_words.csv")
    data_dict = {row[1][f"{LANGUAGE}"]: row[1][f"{TRANSLATE}"] for row in data.iterrows()}

# ---------------------------- Generate flashcards ------------------------------- #

def generate_card():
    global flip_timer
    window.after_cancel(flip_timer)
    card_back.grid_forget()
    card_front.grid(column=0, row=0, columnspan=2)
    l_word = random.choice(list(data_dict.keys()))
    t_word = data_dict[l_word]
    card_front.itemconfig(front_word_text, text=f"{l_word}")
    card_back.itemconfig(back_word_text, text=f"{t_word}")
    flip_timer = window.after(3000, flip_card)

# ---------------------------- Flip flashcards ------------------------------- #

def flip_card():
    card_front.grid_forget()
    card_back.grid(column=0, row=0, columnspan=2)

# ---------------------------- Words to learn functionality ------------------------------- #

def known_word():
    l_word = card_front.itemcget(front_word_text, "text")
    data_dict.pop(l_word)
    l_words = list(data_dict.keys())
    t_words = list(data_dict.values())
    new_data = {LANGUAGE: l_words, TRANSLATE: t_words}
    new_frame = pandas.DataFrame(data=new_data)
    new_frame.to_csv(f"data/{LANGUAGE}_words_to_learn.csv")
    generate_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title(f"{LANGUAGE.capitalize()} Flashcards")
window.config(padx=60, pady=60, bg=BG_COLOR)

# Canvases

card_front = Canvas(height=526, width=800, bg=BG_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_front.create_image(410, 268, image=card_front_image)
front_title_text = card_front.create_text(400, 150, text=f"{LANGUAGE.capitalize()}", fill="black", font=(FONT, 40, "italic"))
front_word_text = card_front.create_text(400, 260, text="Word", fill="black", font=(FONT, 60, "bold"))

card_front.grid(column=0, row=0, columnspan=2)

card_back = Canvas(height=526, width=800, bg=BG_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="images/card_back.png")
card_back.create_image(410, 268, image=card_back_image)
back_title_text = card_back.create_text(400, 150, text=f"{TRANSLATE.capitalize()}", fill="white", font=(FONT, 40, "italic"))
back_word_text = card_back.create_text(400, 260, text="Word", fill="white", font=(FONT, 60, "bold"))


# Buttons

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BG_COLOR, command=known_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BG_COLOR, command=generate_card)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(1000000, flip_card)
generate_card()
window.mainloop()
