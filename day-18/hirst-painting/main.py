# import colorgram as c

# colors = c.extract('spot-painting.jpg',30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
    
# print(rgb_colors)

import turtle as t
import random

color_list = [(208, 159, 108), (223, 206, 117), (136, 173, 194), (215, 231, 240), (39, 107, 140), (137, 184, 147), (13, 52, 76), (219, 87, 63), (145, 80, 71), (70, 165, 119), (30, 129, 106), (125, 80, 96), (10, 58, 50), (55, 153, 180), (196, 
130, 144), (52, 33, 43), (129, 37, 49), (4, 111, 88), (207, 83, 101), (176, 206, 167), (230, 168, 182), (155, 152, 70), (145, 204, 233), (33, 64, 101), (13, 87, 105), (46, 30, 26), (184, 189, 204)]
START_X = -300
START_Y = -300
END_X = 300
END_Y = 300
screen = t.Screen()
t.colormode(255) # pylint: disable=no-member
def draw_dot_line(dot_size, forward_dist, cursor):
    global color_list
    while cursor.pos()[0] < END_X:
        cursor.dot(dot_size, random.choice(color_list))
        if cursor.pos()[0] < END_X:
            cursor.forward(forward_dist)
    return cursor

def reset_at_new_line (cursor):
    cursor.setpos(START_X,cursor.pos()[1])
    return cursor

def next_line(up_dist, cursor):
    cursor.setpos(cursor.pos()[0],cursor.pos()[1]+up_dist)
    reset_at_new_line (cursor)
    return cursor
        
cursor = t.Turtle()
cursor.hideturtle()
cursor.penup()
cursor.speed(0)
cursor.setpos(START_X,START_Y)

num_dot = 10
dot_size = 20
width = END_X + abs(START_X)
height = END_Y + abs(START_Y)
fwr_dist = width / num_dot
up_dist = height / num_dot

while cursor.pos()[1] < END_Y:
    cursor = draw_dot_line(dot_size,fwr_dist,cursor)
    cursor = next_line(up_dist, cursor)
    
screen.exitonclick()