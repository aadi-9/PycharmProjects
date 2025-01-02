import turtle
# import time
# import random

score = 0

wn = turtle.Screen()
wn.title("Snek")
wn.bgcolor("black")
wn.setup(600, 600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)

wn.exitonclick()
