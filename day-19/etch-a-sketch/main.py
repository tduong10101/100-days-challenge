import turtle as t

cursor = t.Turtle()
screen = t.Screen()
screen.listen()

def cursor_action(key_press, action):
    screen.onkey(key=key_press, fun=action)

def move_fwd():
    return cursor.forward(10)

def move_back():
    return cursor.forward(-10)

def turn_r():
    return cursor.setheading(cursor.heading()-30)

def turn_l():
    return cursor.setheading(cursor.heading()+30)

def reset():
    screen.reset()

cursor_action("w",move_fwd)
cursor_action("s",move_back)
cursor_action("a",turn_l)
cursor_action("d",turn_r)
cursor_action("space",reset)
screen.exitonclick()