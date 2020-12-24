from tkinter import *

window = Tk()
window.minsize(width=200,height=50)
window.config(padx=100,pady=25)
window.title("Mile to Km Covertver")
def convert_to_km():
    mile = float(input.get())
    km = round(mile*1.609,2)
    converted_label["text"] = km
#input
input = Entry()
input.configure(width=5)
input.grid(row=0,column=1)
#mile unit label
mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)
#is equal to label
is_eq_label = Label(text="is equal to label")
is_eq_label.grid(row=1,column=0)
#km label
converted_label = Label(text="0")
converted_label.grid(row=1,column=1)
#km unit label
km_label = Label(text="Km")
km_label.grid(row=1,column=2)
#calculate button
cal_button = Button(text="Calculate",command=convert_to_km)
cal_button.grid(row=2,column=1)

window.mainloop()