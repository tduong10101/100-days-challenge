from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
WORD_TO_LEARN = 0
TRANSLATED_WORD = 1
#load data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    try:
        data = pd.read_csv("data/french_words.csv")
    except FileNotFoundError:
        messagebox.showerror(title="No Data Found",message="Unable to find data file")

words_to_learn = data.to_dict(orient="records")
timecounter=None
random_word=None
def remove():
    global random_word, words_to_learn
    words_to_learn.remove(random_word)
    if len(words_to_learn) > 0:
        generate_word()
    else:
        messagebox.showinfo(title="Congraturation!",message="There's no more word to remember!")

def flip_card():
    global random_word
    translated_word=list(random_word.values())[TRANSLATED_WORD]
    translated_language=list(random_word.keys())[TRANSLATED_WORD]
    canvas.itemconfig(word_to_learn,text=translated_word,fill="white")
    canvas.itemconfig(language,text=translated_language,fill="white")
    canvas.itemconfig(card,image=card_back)

def generate_word():
    global timecounter,random_word
    if timecounter:
        window.after_cancel(timecounter)
    random_word = rd.choice(words_to_learn)
    canvas.itemconfig(word_to_learn,fill="black",text=list(random_word.values())[WORD_TO_LEARN])
    canvas.itemconfig(language,fill="black",text=list(random_word.keys())[WORD_TO_LEARN])
    canvas.itemconfig(card,image=card_front)
    timecounter=window.after(3000,flip_card)

#UI
window = Tk()
window.title("Flashy")
window.minsize(width=900,height=726)
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400,263)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
word_to_learn=canvas.create_text(400,263,font=("Arial",60,"bold"))

language=canvas.create_text(400,150,font=("Arial",40,"italic"))

generate_word()

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_btn = Button(image=right_img, highlightthickness=0,bd=0,command=remove)
right_btn.grid(row=1,column=1)

wrong_btn = Button(image=wrong_img, highlightthickness=0,bd=0,command=generate_word)
wrong_btn.grid(row=1,column=0)

window.mainloop()
new_data = pd.DataFrame(words_to_learn)
new_data.to_csv("data/words_to_learn.csv",index=False)