import random
from turtle import Turtle,Screen


screen=Screen()
screen.setup(650,600)
bet=screen.textinput("Make Your Bet","Which turtle will win? Enter colour: ")
print("Your bet is",bet)
colour=["purple","blue","green","yellow","orange","red"]
y=[250,150,50,-50,-150,-250]
allt=[]
for i in range(0,6):
    t1=Turtle()
    t1.color(colour[i])
    t1.shape("turtle")
    t1.penup()
    t1.goto(-300,y[i])
    t1.speed(10)
    allt.append(t1)

if bet:
    race_on = True

while race_on:

    for t in allt:
        dist = random.randint(0, 20)
        t.forward(dist)
        if t.xcor() > 300:
            print(f"{t.pencolor()} has won!!")
            if bet == t.pencolor():
                print("you have won")
            else:
                print("you have lost")
            race_on = False
            break


screen.exitonclick()
