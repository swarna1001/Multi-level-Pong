import turtle
import tkinter as tk
from tkinter import Button
from tkinter import ttk

wn = turtle.Screen()
wn.setup(width=1000, height=700)
wn.bgcolor("black")
wn.tracer(0)
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
pen = turtle.Turtle()
ball = turtle.Turtle()
ball2 = turtle.Turtle()
ball3 = turtle.Turtle()


def screen():
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=1000, height=700)
    wn.tracer(0)
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 130)
    pen.write("PONG", align="center", font=("Times New Roman", 38, "bold"))
    pen.goto(0, 0)
    pen.write("Levels:", align="center", font=("Courier", 28, "bold"))
    pen.goto(0, -70)
    pen.write("Easy (press e)", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -120)
    pen.write("Medium (press m)", align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -170)
    pen.write("Hard (press h)", align="center", font=("Courier", 24, "normal"))


def replay():
    wn.reset()
    screen()
    wn.onkeypress(easy, "e")
    wn.onkeypress(medium, "m")
    wn.onkeypress(hard, "h")


# display options
def options():
    pen.color("white")
    pen.goto(0, -310)
    pen.write("Replay (press r)", align="center", font=("Courier", 24, "normal"))


# score display final window
def player_a_is_winner():
    pen.clear()
    pen.color("green")
    pen.goto(0, 140)
    pen.clear()
    pen.write(f"Player A won!", align="center", font=("Courier", 28, "bold"))
    pen.goto(0, 230)
    pen.write(f"GAME OVER! ", align="center", font=("Courier", 28, "bold"))


def player_b_is_winner():
    pen.clear()
    pen.color("green")
    pen.goto(0, 140)
    pen.write(f"Player B won!", align="center", font=("Courier", 28, "bold"))
    pen.goto(0, 230)
    pen.write(f"GAME OVER !", align="center", font=("Courier", 28, "bold"))


def score_display():
    # pen
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 270)
    pen.write("Player A: 0                  Player B: 0", align="center", font=("Courier", 24, "normal"))


screen()


def create_paddle(paddle_width):
    # paddle A
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=paddle_width, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-450, 0)

    # paddle B
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=paddle_width, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(450, 0)


def paddle_movement():
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 90
        paddle_a.sety(y)
        if y > 150:
            paddle_a.sety(150)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 90
        paddle_a.sety(y)
        if y < -180:
            paddle_a.sety(-180)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 90
        paddle_b.sety(y)
        if y > 150:
            paddle_b.sety(150)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 90
        paddle_b.sety(y)
        if y < -180:
            paddle_b.sety(-180)

    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")


def win_at(winning_score):
    pen.goto(0, -320)
    pen.write("Win at: {} ".format(winning_score), align="center", font=("Courier", 22, "normal"))


def easy_game_loop(color, winning_score):
    ball.speed(0)
    ball.shape("circle")
    ball.color(color)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2.9
    ball.dy = 2.9

    # score
    score_a = 0
    score_b = 0

    while True:
        wn.update()
        paddle_movement()
        # movement ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # paddle and ball  collisions

        if ball.xcor() > 426 and paddle_b.ycor() + 125 > ball.ycor() > paddle_b.ycor() - 125:
            ball.dx *= -1

        elif ball.xcor() < -426 and (paddle_a.ycor() + 125 > ball.ycor() > paddle_a.ycor() - 125):
            ball.dx *= -1

        # border checking ball
        if ball.ycor() > 260:
            ball.sety(260)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 465:
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

    ball.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()


def medium_game_loop(b1_color, b2_color, winning_score):
    ball.speed(0)
    ball.shape("circle")
    ball.color(b1_color)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1.9
    ball.dy = 1.9

    ball2.speed(0)
    ball2.shape("circle")
    ball2.color(b2_color)
    ball2.penup()
    ball2.goto(0, 0)
    ball2.dx = 2.4
    ball2.dy = 2.4

    # score
    score_a = 0
    score_b = 0

    while True:
        wn.update()
        paddle_movement()
        # movement ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # movement ball 1
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)

        # paddle and ball  collisions

        if ball.xcor() > 430 and paddle_b.ycor() + 120 > ball.ycor() > paddle_b.ycor() - 120:
            ball.dx *= -1

        elif ball.xcor() < -430 and (paddle_a.ycor() + 120 > ball.ycor() > paddle_a.ycor() - 120):
            ball.dx *= -1

        # paddle and ball2 collision
        if ball2.xcor() > 430 and paddle_b.ycor() + 120 > ball2.ycor() > paddle_b.ycor() - 120:
            ball2.dx *= -1

        elif ball2.xcor() < -430 and (paddle_a.ycor() + 120 > ball2.ycor() > paddle_a.ycor() - 120):
            ball2.dx *= -1

        # border checking ball
        if ball.ycor() > 260:
            ball.sety(260)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball2.ycor() > 260:
            ball2.sety(260)
            ball2.dy *= -1

        if ball2.ycor() < -290:
            ball2.sety(-290)
            ball2.dy *= -1

        if ball.xcor() > 465:
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball2.xcor() > 465:
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball2.goto(0, 0)
            ball2.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball2.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball2.goto(0, 0)
            ball2.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

    ball.hideturtle()
    ball2.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()


def hard_game_loop(b1_color, b2_color, b3_color, winning_score):
    ball.speed(0)
    ball.shape("circle")
    ball.color(b1_color)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1.9
    ball.dy = 1.9

    ball2.speed(0)
    ball2.shape("circle")
    ball2.color(b2_color)
    ball2.penup()
    ball2.goto(0, 0)
    ball2.dx = 2.4
    ball2.dy = 2.4

    ball3.speed(0)
    ball3.shape("circle")
    ball3.color(b3_color)
    ball3.penup()
    ball3.goto(0, 0)
    ball3.dx = 1.6
    ball3.dy = 1.6

    # score
    score_a = 0
    score_b = 0

    while True:
        wn.update()
        paddle_movement()
        # movement ball 1
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # movement ball 2
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)

        # movement ball 3
        ball3.setx(ball3.xcor() + ball3.dx)
        ball3.sety(ball3.ycor() + ball3.dy)

        # paddle and ball1  collisions

        if ball.xcor() > 430 and paddle_b.ycor() + 120 > ball.ycor() > paddle_b.ycor() - 120:
            ball.dx *= -1

        elif ball.xcor() < -430 and (paddle_a.ycor() + 120 > ball.ycor() > paddle_a.ycor() - 120):
            ball.dx *= -1

        # paddle and ball2 collision
        if ball2.xcor() > 430 and paddle_b.ycor() + 120 > ball2.ycor() > paddle_b.ycor() - 120:
            ball2.dx *= -1

        elif ball2.xcor() < -430 and (paddle_a.ycor() + 120 > ball2.ycor() > paddle_a.ycor() - 120):
            ball2.dx *= -1

        # paddle and ball 3 collisions

        if ball3.xcor() > 430 and paddle_b.ycor() + 150 > ball3.ycor() > paddle_b.ycor() - 150:
            ball3.dx *= -1

        elif ball3.xcor() < -430 and (paddle_a.ycor() + 150 > ball3.ycor() > paddle_a.ycor() - 150):
            ball3.dx *= -1

        # border checking ball
        if ball.ycor() > 260:
            ball.sety(260)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball2.ycor() > 260:
            ball2.sety(260)
            ball2.dy *= -1

        if ball2.ycor() < -290:
            ball2.sety(-290)
            ball2.dy *= -1

        if ball3.ycor() > 260:
            ball3.sety(260)
            ball3.dy *= -1

        if ball3.ycor() < -290:
            ball3.sety(-290)
            ball3.dy *= -1

        if ball.xcor() > 465:
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball2.xcor() > 465:
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball2.goto(0, 0)
            ball2.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball2.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball2.goto(0, 0)
            ball2.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball3.xcor() > 465:  # BALL 3
            score_a += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball3.goto(0, 5)
            ball3.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

        if ball3.xcor() < -465:
            score_b += 1
            pen.clear()
            pen.goto(0, 270)
            pen.write("Player A: {}                 Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            win_at(winning_score)
            ball3.goto(0, 5)
            ball3.dx *= -1

            if score_a == winning_score and score_a > score_b:
                player_a_is_winner()
                options()
                break

            elif score_b == winning_score and score_b > score_a:
                player_b_is_winner()
                options()
                break

    ball.hideturtle()
    ball2.hideturtle()
    ball3.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()


def easy():
    wn.reset()
    create_paddle(11)
    score_display()
    easy_game_loop("red", 20)
    wn.onkeypress(replay, "r")


def medium():
    wn.reset()
    create_paddle(11)
    score_display()
    medium_game_loop("red", "yellow", 25)
    wn.onkeypress(replay, "r")


def hard():
    wn.reset()
    create_paddle(13)
    score_display()
    hard_game_loop("white", "white", "white", 20)
    wn.onkeypress(replay, "r")


wn.listen()
wn.onkeypress(easy, "e")
wn.onkeypress(medium, "m")
wn.onkeypress(hard, "h")

while True:
    wn.update()
