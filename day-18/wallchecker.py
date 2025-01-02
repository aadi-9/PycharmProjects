import random
import turtle
from turtle import Turtle

def wall_checker(self):
    # print(self.xcor(), self.ycor())

    if self.xcor() > 300:
        self.goto(290, self.ycor())
    elif self.xcor() < -300:
        self.goto(-290, self.ycor())

    if self.ycor() > 300:
        self.goto(self.xcor(), 290)
    elif self.ycor() < -300:
        self.goto(self.xcor(), -290)

def randcolour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    y=random.randint(0,255)
    rgy=(r,g,y)
    return rgy

x=0
leo = Turtle()
turtle.colormode(255)
leo.shape("turtle")
leo.color("aquamarine4")
leo.speed(10)
# angle=int(input("enter gap"))
# while x!=int(360/angle):
#     wall_checker(leo)
#     leo.pencolor(randcolour())
#     leo.circle(100)
#     leo.left(angle)
#     x+=1
# while shape!=75:
#     wall_checker(leo)
#     #c=random.choice(["firebrick", "green", "royal blue", "medium purple", "yellow2", "orange","magenta","pink",
#      #                "medium spring green","lavender","VioletRed3","SkyBlue2"])
#     x=random.randint(1,4)
#     sh=random.randint(1,2)
#     ang=random.randint(10,360)
#     l=random.choice([100,150,200,250])
#     leo.pencolor(randcolour())
#     if sh==1:
#         match x:
#             case 1:
#                 leo.forward(l)
#             case 2:
#                 leo.back(l)
#             case 3:
#                 leo.left(90)
#                 leo.forward(l)
#             case 4:
#                 leo.right(90)
#                 leo.forward(l)
#     else:
#         match x:
#             case 1:
#                 leo.circle(l,ang)
#             case 2:
#                 leo.circle(l,180-ang)
#             case 3:
#                 leo.left(90)
#                 leo.circle(l,ang)
#             case 4:
#                 leo.right(90)
#                 leo.circle(l,ang)
#
#     shape+=1

