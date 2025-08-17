import turtle
import winsound  # Only works on Windows for sound
import time

# --- Screen setup ---
win = turtle.Screen()
win.title("Pong Game - Upgraded")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# --- Score ---
score_a = 0
score_b = 0
winning_score = 5  # Game ends when a player reaches this score

# --- Paddle A ---
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# --- Paddle B ---
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# --- Ball ---
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# --- Pen for score ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# --- Functions ---
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y < 250:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -240:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y < 250:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y > -240:
        paddle_b.sety(y)

def play_sound(sound_file):
    try:
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    except:
        pass  # Skip sound on non-Windows systems

# --- Keyboard bindings ---
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# --- Main game loop ---
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_sound("bounce.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound("bounce.wav")

    # Right border (Player A scores)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -0.15  # Reset direction
        ball.dy = 0.15
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        play_sound("score.wav")
        time.sleep(0.5)

    # Left border (Player B scores)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 0.15
        ball.dy = 0.15
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        play_sound("score.wav")
        time.sleep(0.5)

    # Paddle collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1.1  # Increase speed by 10% after hit
        play_sound("bounce.wav")

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1.1  # Increase speed by 10% after hit
        play_sound("bounce.wav")

    # Win condition
    if score_a >= winning_score:
        pen.clear()
        pen.write("Player A Wins!", align="center", font=("Courier", 36, "bold"))
        break

    if score_b >= winning_score:
        pen.clear()
        pen.write("Player B Wins!", align="center", font=("Courier", 36, "bold"))
        break

win.mainloop()
