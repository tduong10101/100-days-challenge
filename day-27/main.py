import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

#label
my_label = tk.Label(text="this is my label", font=("Arial",24))
my_label.grid(row=0, column=0)

#button
def button_clicked():
    my_label["text"] = input.get()

button = tk.Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)


new_button = tk.Button(text="new button", command=button_clicked)
new_button.grid(row=0, column=2)
#entry

input = tk.Entry(width=10)
input.grid(row=2,column=3)

window.mainloop()