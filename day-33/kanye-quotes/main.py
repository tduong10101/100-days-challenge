from tkinter import *
import tkinter.font as tkFont
import requests
import json

def get_txt_size():
    x1,y1,x2,y2 = canvas.bbox(quote_text)
    width = x2-x1
    height = y2-y1
    return {"width":width,"height":height}

def get_quote():
    font_style["size"] = 30
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text=quote)
    text_size = get_txt_size()
    while (text_size["width"] > 150 and text_size["height"] > 207):
        font_style["size"] -= 1
        canvas.itemconfig(quote_text,font=font_style)
        text_size = get_txt_size()


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
font_style = tkFont.Font(family="Arial",size=30,weight="bold")
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=font_style, fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()