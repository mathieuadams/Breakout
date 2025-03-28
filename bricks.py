from turtle import Turtle

class Bricks(Turtle):
    def __init__(self,coordinate, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.goto(coordinate)

