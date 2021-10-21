import turtle
# Game Window Setup
game_window = turtle.Screen()
game_window.title("Pong in Turtle")
game_window.bgcolor("black")
game_window.setup(width=800, height=600) # center of window is 0,0. Going right/up is positive and left/down is negative numbers
game_window.tracer(0)


# Paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # default value is 20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 ,stretch_len=1) # width is vertical, length is horizontal. numbers given are multiplied by the default value
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 ,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.xspeed = 1.2
paddle_b.yspeed = 1.2

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle") # default value is 20px
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.xspeed = 1
ball.yspeed = -1

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 37
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 37
    paddle_a.sety(y)

def paddle_b_up():
     y = paddle_b.ycor()
     y += 37
     paddle_b.sety(y)

def paddle_b_down():
     y = paddle_b.ycor()
     y -= 37
     paddle_b.sety(y)

# Key Presses
game_window.listen()
game_window.onkeypress(paddle_a_up, "w")
game_window.onkeypress(paddle_a_down, "s")
game_window.onkeypress(paddle_b_up, "Up")
game_window.onkeypress(paddle_b_down, "Down")
# Game Loop
while True:

    # Paddle A Border
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    
    # Paddle B Border
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    
    # Ball Movement
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.xspeed *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.xspeed *= -1

    game_window.update()