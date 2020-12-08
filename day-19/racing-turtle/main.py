import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
colors = ["red","orange","yellow","green","blue","purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color ({', '.join(colors)}): ")

turtle_list = []
start_y = -100
for color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    start_y += 50
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:    
    for turtle in turtle_list:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            is_race_on = False
            break
        
screen.exitonclick()