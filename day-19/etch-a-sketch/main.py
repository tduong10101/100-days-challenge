import turtle as t

cursor = t.Turtle()
screen = t.Screen()
screen.listen()

def cursor_action(key_press, action):
    screen.onkey(key=key_press, fun=action)

def move_fwd():
    return cursor.forward(10)

cursor_action("w",move_fwd)

screen.exitonclick()