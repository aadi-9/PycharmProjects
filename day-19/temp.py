from turtle import Turtle,Screen

leo = Turtle()
screen = Screen()


def move_fd():
    leo.forward(10)


def move_bk():
    leo.back(10)


def move_rt():
    leo.right(10)


def move_lf():
    leo.left(10)


def clear():
    leo.home()
    leo.clear()


screen.listen()
screen.onkey(move_fd,"w")
screen.onkey(move_bk,"s")
screen.onkey(move_rt,"d")
screen.onkey(move_lf,"a")
screen.onkey(clear,"c")
screen.exitonclick()

