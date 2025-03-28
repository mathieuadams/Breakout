from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(coordinate)
        self.score = 0
        self.style=('Courier', 30, 'normal')
        self.write(f"{self.score}", font=self.style, align='center')
        self.hideturtle()

    def addpoint(self):
        self.clear()
        self.score +=1
        self.write(f"{self.score}", font=self.style, align='center')

    def reset_score(self):
        self.clear()
        self.score =0
        self.write(f"{self.score}", font=self.style, align='center')


