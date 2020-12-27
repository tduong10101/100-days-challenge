from tkinter import *
import random
import pyperclip
# generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= 6
    nr_symbols = 4
    nr_numbers = 4

    password = [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]
    password_str = "".join(password)
    random.shuffle(password)
    password_entr.delete(0,END)
    password_entr.insert(0,password_str)
    pyperclip.copy(password_str)


# save data
def save_data():
    web = web_entr.get()
    username = username_entr.get()
    password = password_entr.get()

    text = f"{web} | {username} | {password}\n"
    with open("data.txt","a") as f:
        f.write(text)
        web_entr.delete(0,END)
        password_entr.delete(0,END)

# ui
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=124,height=200)
canvas.create_image(62,100,image=logo_img)
canvas.grid(row=0,column=1)

web_lbl = Label(text="Website: ")
web_lbl.grid(row=1,column=0,sticky="e")

web_entr = Entry(width=40)
web_entr.grid(row=1,column=1,columnspan=2,sticky="w")

username_lbl = Label(text="Username/Email: ")
username_lbl.grid(row=2,column=0,sticky="e")

username_entr = Entry(width=40)
username_entr.grid(row=2,column=1,sticky="w",columnspan=2)
username_entr.insert(0,"tduong10101@gmail.com")

password_lbl = Label(text="Password: ")
password_lbl.grid(row=3,column=0,sticky="e")

password_entr = Entry(width=21)
password_entr.grid(row=3,column=1,sticky="w")

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2,sticky="w")

add_button = Button(text="Add",width=33,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()