from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
import html

r = requests.get("https://opentdb.com/api.php?amount=20&category=15&difficulty=easy&type=boolean")
r_json = r.json()
r_result = r_json["results"]

questions_bank = []
for question in r_result:
    questions_bank.append(Question(html.unescape(question['question']), question['correct_answer']))

quiz = QuizBrain(questions_bank)
while quiz.still_has_questions():    
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")