# A flash card program for learning french words
from tkinter import *
import pandas as pd
import random
# read the csv that contains the words to learn and convert it to a dictionary. if the file is not available, then read the default file
try:
    words_to_l_df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    french_df = pd.read_csv("flash_card/data/french_words.csv")
    words_to_l = french_df.to_dict(orient="records")
else:
    words_to_l = words_to_l_df.to_dict(orient="records")

random_word = {}


def random_french_word():
    """ generates and displays random french words from the dictionary """
    global random_word, flip_timer, words_to_l
    window.after_cancel(flip_timer)
    card_front.itemconfig(title, text="French", fill="black")
    card_front.itemconfig(card_displayed, image=photo_cf)
    random_word = random.choice(words_to_l)
    random_french_w = random_word["French"]
    card_front.itemconfig(word_to_learn, text=random_french_w, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """flips the card to the english interpretation of the word"""
    global random_word
    card_front.itemconfig(title, text="English", fill="white")
    card_front.itemconfig(card_displayed, image=photo_cb)
    random_english_w = random_word["English"]
    card_front.itemconfig(word_to_learn, text=random_english_w, fill="white")


def right_button_function():
    """ changes the word to a new one and deletes it from the words_to_learn dictionary"""
    random_french_word()
    words_to_l.remove(random_word)
    if len(words_to_l) == 0:
        card_front.itemconfig(word_to_learn, text="You have learnt all the words", fill="black")
    else:
        data = pd.DataFrame(words_to_l)
        data.to_csv("words_to_learn.csv", index=False)


def wrong_button_function():
    """changes the word to a new word"""
    random_french_word()
    if len(words_to_l) == 0:
        card_front.itemconfig(word_to_learn, text="You have learnt all the words", fill="black")
    else:
        data = pd.DataFrame(words_to_l)
        data.to_csv("words_to_learn.csv", index=False)

BACKGROUND = "cyan"
# set up the display window
window = Tk()
window.title("Language Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND)
flip_timer = window.after(3000, flip_card)

# set up the canvas environment
card_front = Canvas(width=800, height=526, highlightthickness=0)
photo_cf = PhotoImage(file="flash_card/images/card_front.png")
photo_cb = PhotoImage(file="flash_card/images/card_back.png")
card_displayed = card_front.create_image(400, 263, image=None)
card_front.grid(row=0, column=0, columnspan=2)
card_front.config(bg=BACKGROUND, highlightthickness=0)
title = card_front.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_to_learn = card_front.create_text(400, 263, text="", font=("Arial", 60, "bold"), tags="word")

# buttons
right_image = PhotoImage(file="flash_card/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_button_function)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="flash_card/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_button_function)
wrong_button.grid(row=1, column=1)

random_french_word()

window.mainloop()
