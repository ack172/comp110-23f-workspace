"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(10, 10)
leo.pendown()


leo.pencolor(0, 0, 0)
leo.begin_fill()

i: int = 0

while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.fillcolor("pink")
leo.end_fill()
leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(10, 10)
bob.pendown()
bob.speed(0)

idx: int = 0
side_length: int = 300
while idx < 10:
    bob.forward(side_length)
    bob.left(120)
    i += 1
    side_length *= 0.97
done()
