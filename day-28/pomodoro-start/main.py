from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = .1
SEC_PER_MIN = 60
repl = 0
timer_after = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repl, timer_after
    repl = 0
    window.after_cancel(timer_after)
    chkmarks_label['text'] = ""
    title_label['text'] = "Timer"
    canvas.itemconfig(time_counter,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global repl
    repl += 1
    if repl % 8 == 0:
        timer = LONG_BREAK_MIN * SEC_PER_MIN
        title_text = "Break"
        fg_color = RED
    elif repl % 2 == 0:
        timer = SHORT_BREAK_MIN * SEC_PER_MIN
        title_text = "Break"
        fg_color = PINK
    else:
        timer = WORK_MIN * SEC_PER_MIN
        title_text = "Work"
        fg_color = GREEN
    timer = int(timer)
    title_label.config(text=title_text, fg=fg_color)
    count_down(timer)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec = count%60
    time_text = f"{min}:{sec:02d}"
    canvas.itemconfig(time_counter,text=time_text)
    work_session = math.floor(repl/2)
    chkmark_text = ""
    for _ in range(work_session):
        chkmark_text += "✓"
    chkmarks_label['text'] = chkmark_text
    if count > 0:
        global timer_after
        timer_after = window.after(1000, count_down, count-1)
    else:
        start_count()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, bd=0,highlightthickness=0, relief='ridge')
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
time_counter = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(row=0,column=1)

start_button = Button(text="Start",command=start_count)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2,column=2)

chkmarks_label = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
chkmarks_label.grid(row=3,column=1)

window.mainloop()