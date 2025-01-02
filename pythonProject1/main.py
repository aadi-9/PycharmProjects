from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
scoreboard = ScoreBoard()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

gameon = True
x = 0.1
while gameon:
    time.sleep(x)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.scoreinc1()
        ball.goto(0, 0)
        x *= 0.9
        ball.bounce_x()

    if ball.xcor() < -380:
        scoreboard.scoreinc2()
        ball.goto(0, 0)
        x *= 0.9
        ball.bounce_x()

    if x <= 0:
        scoreboard.gameover()
        gameon = False

screen.exitonclick()
