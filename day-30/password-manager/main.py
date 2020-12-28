from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
# check password
def search_site():
    try:
        f = open("data.json")
    except FileNotFoundError:
        messagebox.showinfo(title="No data",message="Data file not exist!")
    else:
        data = json.load(f)
        f.close()
        web = web_entr.get()
        if not web.strip():
            messagebox.showinfo(title="Missing data",message="Please fill in website field")
        else:
            if web not in data:
                messagebox.showinfo(title="Site not found",message=f"No details for {web} exists.")
            else:
                search_result = data[web]
                username = search_result["username"]
                password = search_result["password"]
                messagebox.showinfo(title=web,message=f"Username: {username}\nPassword: {password}")
# save data
def save_data():
    web = web_entr.get()
    username = username_entr.get()
    password = password_entr.get()
    new_data = {
        web: {
            "username":username,
            "password":password
        }
    }
    if not web.strip() or not username.strip() or not password.strip():
        messagebox.showinfo(title="Missing Data",message="Please fill in all fields")
    else:
        try:
            f = open("data.json","r")
        except FileNotFoundError:
            data = new_data
        else:
            data = json.load(f)
            data.update(new_data)
            f.close()
        finally:
            with open("data.json","w") as f:
                json.dump(data, f,indent=4)
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

web_entr = Entry(width=21)
web_entr.grid(row=1,column=1,sticky="w")

search_btn = Button(text="Search",width=15,command=search_site)
search_btn.grid(row=1,column=2,sticky="w")

username_lbl = Label(text="Username/Email: ")
username_lbl.grid(row=2,column=0,sticky="e")

username_entr = Entry(width=40)
username_entr.grid(row=2,column=1,sticky="w",columnspan=2)
username_entr.insert(0,"tduong10101@gmail.com")

password_lbl = Label(text="Password: ")
password_lbl.grid(row=3,column=0,sticky="e")

password_entr = Entry(width=21)
password_entr.grid(row=3,column=1,sticky="w")

password_button = Button(text="Generate Password",command=generate_password,width=15)
password_button.grid(row=3,column=2,sticky="w")

add_button = Button(text="Add",width=33,command=save_data)
add_button.grid(row=4,column=1,columnspan=2,sticky="e")

window.mainloop()