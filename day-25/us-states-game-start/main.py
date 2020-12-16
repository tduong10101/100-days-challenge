import turtle as t
import pandas as pd

# load data
data = pd.read_csv("50_states.csv")
# create turtle object
drawer = t.Turtle()
drawer.penup()
drawer.hideturtle()

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image) # pylint: disable=no-member
all_states = data.state.to_list()
guess_states = []
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 State Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state in all_states:        
        answer_state_row = data[data.state == answer_state]
        x = int(answer_state_row.x)
        y = int(answer_state_row.y)
        draw_coor = (x, y) 
        drawer.setpos(draw_coor)
        drawer.write(f"{answer_state}",False,align="Center",font=("Arial",8,"bold"))
        guess_states.append(answer_state_row)
    elif answer_state == "Exit":
        # state to learn csv file
        state_to_learn = []
        for state in all_states:
            if state not in guess_states:
                state_to_learn.append(state)
                
        state_to_learn_data = pd.DataFrame(state_to_learn)
        state_to_learn_data.columns = ['state']
        state_to_learn_data.to_csv("state_to_learn.csv")
        break

