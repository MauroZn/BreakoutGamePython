from turtle import Screen, Turtle
from player_bar import PlayerBar
from ball import Ball
from bricks_manager import BricksManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=500, height=800)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

player_bar = PlayerBar()
ball = Ball()
bricks_manager = BricksManager()
scoreboard = Scoreboard()
start_text = Turtle()

ball_launched = False
game_is_on = True
ball_far = False

def launch_ball():
    global ball_launched
    ball_launched = True
    start_text.clear()

start_text.hideturtle()
start_text.color("white")
start_text.penup()
start_text.goto(0, 0)
start_text.write("Press UP to start the game.",align= "center", font=("Arial", 18, "bold"))

screen.listen()
screen.onkey(player_bar.left, "Left")
screen.onkey(player_bar.right, "Right")
screen.onkey(launch_ball, "Up")

while game_is_on:

    if (abs(ball.xcor() - player_bar.xcor()) < 50 and
        abs(ball.ycor() - player_bar.ycor()) < 25 and
        180 < ball.heading() < 360 and
        ball_far):
        ball.bounce_up()
        ball_far = False

    if ball.distance(player_bar) > 50:
        ball_far = True

    if ball_launched:
        ball.start_ball()

    screen.update()
    time.sleep(0.05)

    if ball.xcor() >= 240:
        ball.setx(240)
        ball.bounce_left()
    elif ball.xcor() <= -240:
        ball.setx(-240)
        ball.bounce_right()
    elif ball.ycor() >= 390:
        ball.sety(390)
        ball.bounce_down()
    elif ball.ycor() <= -390:
        scoreboard.game_over()
        game_is_on = False

    if bricks_manager.all_bricks:
        for brick in bricks_manager.all_bricks:
            if ball.distance(brick) < 35:
                brick.goto(1000, 1000)
                bricks_manager.all_bricks.remove(brick)
                scoreboard.increase_score()
                ball.bounce_down()
                break
    else:
        scoreboard.winner()
        game_is_on = False

screen.exitonclick()
