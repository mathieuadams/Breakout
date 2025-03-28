
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from bricks import Bricks
import time

def create_new_bricks():
    all_bricks = []
    for i in range(-275, 325, 50):
        brick = Bricks((i, 300), "green")
        brick1 = Bricks((i, 275), "green")
        brick2 = Bricks((i, 250), "blue")
        brick21 = Bricks((i, 225), "blue")
        brick3 = Bricks((i, 200), "red")
        brick31 = Bricks((i, 175), "red")
        all_bricks.append(brick)
        all_bricks.append(brick1)
        all_bricks.append(brick2)
        all_bricks.append(brick21)
        all_bricks.append(brick3)
        all_bricks.append(brick31)
    return all_bricks

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout")
game_is_on = True
screen.tracer(0)
all_bricks = create_new_bricks()

paddle = Paddle((0,-340))
ball = Ball()
score = ScoreBoard((0,350))


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")



while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.1)
    if ball.xcor()< -280 or ball.xcor()> 280:
        ball.bounce_x()
    if ball.ycor() > 360:
        ball.bounce_y()
    if ball.distance(paddle) < 40 and ball.ycor()< -300 and ball.paddle_hit_ready :
        ball.bounce_y()
        ball.paddle_hit_ready = False
    if ball.ycor() > -250:
        ball.paddle_hit_ready = True


    for brick in all_bricks :
        if ball.distance(brick)<40:
            ball.bounce_y()

            brick.goto(5000,5000)
            score.addpoint()




    if ball.ycor() < -400:
        ball.reset()
        score.reset_score()

        for brick in all_bricks:
            brick.goto(5000,5000)
        all_bricks = create_new_bricks()












screen.exitonclick()