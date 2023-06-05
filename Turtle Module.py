import turtle

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])


def draw_circle(Size):
    turtle.pencolor(next(colors))
    turtle.circle(Size)
    draw_circle(Size+5)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)


