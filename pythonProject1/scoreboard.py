from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update()

    def update(self):
        self.goto(-100, 250)
        self.write({self.score1}, False, ALIGN, FONT)
        self.goto(100, 250)
        self.write({self.score2}, False, ALIGN, FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, ALIGN, FONT)

    def scoreinc1 (self):
        self.score1 += 1
        self.clear()
        self.update()

    def scoreinc2 (self):
        self.score2 += 1
        self.clear()
        self.update()
