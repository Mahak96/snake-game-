# Simple Snake Game in Python 3

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []

# Pen for writing score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to change direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()  # Update the screen

    # Check for a collision with the border (wrap around the screen)
    if head.xcor() > 290:
        head.setx(-290)  # Wrap around to the left side
    elif head.xcor() < -290:
        head.setx(290)  # Wrap around to the right side

    if head.ycor() > 290:
        head.sety(-290)  # Wrap around to the bottom
    elif head.ycor() < -290:
        head.sety(290)  # Wrap around to the top

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay (make the snake move faster)
        delay -= 0.001

        # Increase the score
        score += 1

        # Update high score
        if score > high_score:
            high_score = score

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # Move the snake

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:  # If the head collides with a body segment
            time.sleep(1)  # Pause for 1 second
            head.goto(0, 0)  # Reset the head position to the center
            head.direction = "stop"  # Stop the snake's movement

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move all body segments off-screen
            segments.clear()  # Clear the segments list

            # Reset the score
            score = 0

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)  # Slow down the game loop for smooth movement

wn.mainloop()  # Keep the window open


 
 
 
 
 

 
