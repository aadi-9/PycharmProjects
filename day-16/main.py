# from turtle import Turtle, Screen
#
# leo = Turtle()
# print(leo)
# leo.shape("turtle")
# leo.color("aquamarine4")
# leo.fd(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "r"
print(table)


