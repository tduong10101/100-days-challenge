from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        
        self.score = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1,padx=20,pady=20)
        
        self.main_cv = Canvas(width=300,height=250)
        self.main_cv.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        
        self.question = self.main_cv.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",15,"italic"))
        self.get_next_question()
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=self.true_img,
            highlightthickness=0,
            command=self.true_cmd
        )
        self.true_btn.grid(row=2,column=0,padx=20,pady=20)
        
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=self.false_img,
            highlightthickness=0,
            command=self.false_cmd
        )
        self.false_btn.grid(row=2,column=1,padx=20,pady=20)
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.main_cv.config(bg="white")
        if self.quiz.still_has_questions():            
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.main_cv.itemconfig(self.question,text=q_text)
        else:
            self.main_cv.itemconfig(self.question,text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    def true_cmd(self):
        self.give_feedback(self.quiz.check_answer("true"))
    
    def false_cmd(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self, is_right):
        
        if is_right:
            self.main_cv.config(bg="green")
        else:
            self.main_cv.config(bg="red")
        self.window.after(1000,self.get_next_question)