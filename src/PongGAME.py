import turtle
import pygame

# Initialize the turtle screen and pygame mixer
wn = turtle.Screen()
pygame.mixer.init()

# Load the sound effect file
hit_sound = pygame.mixer.Sound("static/throwing-a-rock-on-ice.mp3")

# Set up the turtle screen
wn.title("Pong by Kumar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Initialize scores
score_A = 0
score_B = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("white")
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("white")
paddleB.penup()
paddleB.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.shapesize(stretch_wid=1, stretch_len=1)
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.5
Ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions for paddle movement
def paddle_A_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddle_A_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddle_B_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddle_B_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")

# Main game loop
while True:
    wn.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (340 < Ball.xcor() < 350) and (paddleB.ycor() - 50 < Ball.ycor() < paddleB.ycor() + 50):
        Ball.setx(340)
        Ball.dx *= -1
        hit_sound.play()

    if (-350 < Ball.xcor() < -340) and (paddleA.ycor() - 50 < Ball.ycor() < paddleA.ycor() + 50):
        Ball.setx(-340)
        Ball.dx *= -1
        hit_sound.play()
