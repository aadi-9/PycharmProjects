import turtle
from turtle import Turtle,Screen
import random
#import colorgram

#colours=colorgram.extract("leos_colour.jpeg",10)
# for color in colours:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r,g,b))
# print(rgb)

rgb=[(253, 251, 249), (216, 229, 235), (146, 165, 178), (232, 243, 242), (248, 235, 242), (216, 124, 134),
     (120, 194, 183), (73, 85, 99), (213, 171, 192), (221, 206, 144)]
leo = Turtle()
turtle.colormode(255)
leo.shape("turtle")
leo.color("aquamarine4")
leo.speed(10)
leo.setheading(225)
leo.penup()
leo.fd(450)
leo.setheading(0)
leo.pendown()
x,y=0,0
screen = Screen()
screen.bgcolor("navajo white")

while y!=5:
    for i in range (5):
        leo.dot(70,random.choice(rgb))
        leo.penup()
        leo.fd(100)
        leo.pendown()
        x+=1
    leo.setheading(90)
    leo.penup()
    leo.fd(100)
    leo.setheading(180)
    leo.fd(500)
    leo.setheading(0)
    leo.pendown()
    y+=1



screen.exitonclick()


