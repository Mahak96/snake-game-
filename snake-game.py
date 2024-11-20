import turtle  # Import the turtle module for graphics
import time  # Import time module to control game speed
import random  # Import random module to place food randomly

delay = 0.1  # Initial game delay, controls the snake's speed

# Score variables
score = 0  # Variable to keep track of the player's current score
high_score = 0  # Variable to keep track of the highest score

# Set up the screen
wn = turtle.Screen()  # Create the screen object
wn.title("Snake Game")  # Set the window title
wn.bgcolor("black")  # Set the background color of the window
wn.setup(width=600, height=600)  # Set the dimensions of the screen
wn.tracer(0)  # Turn off automatic screen updates to manually control them

# Snake head setup
head = turtle.Turtle()  # Create a new turtle object for the snake head
head.speed(0)  # Set the speed of the head to maximum (fastest)
head.shape("circle")  # Set the shape of the head to a circle
head.color("red")  # Set the color of the head to red
head.penup()  # Lift the pen so the turtle doesn't draw lines
head.goto(0, 0)  # Set the initial position of the head at the center of the screen
head.direction = "stop"  # Initially set the snake's movement direction to "stop"

# Snake food setup
food = turtle.Turtle()  # Create a new turtle object for the food
food.speed(0)  # Set the speed of the food to maximum (fastest)
food.shape("circle")  # Set the shape of the food to a circle
food.color("yellow")  # Set the color of the food to yellow
food.penup()  # Lift the pen so the turtle doesn't draw lines
food.goto(0, 100)  # Set the initial position of the food

# List to hold the body segments of the snake
segments = []  # Empty list to store the body parts of the snake

# Pen for displaying score
pen = turtle.Turtle()  # Create a new turtle object for displaying text
pen.speed(0)  # Set the speed of the pen to maximum (fastest)
pen.shape("square")  # Set the pen's shape to square (not important here)
pen.color("white")  # Set the pen's color to white
pen.penup()  # Lift the pen so it doesn't draw lines
pen.hideturtle()  # Hide the turtle cursor
pen.goto(0, 260)  # Set the initial position of the score display
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))  # Display initial scores

# Functions to change direction based on user input
def go_up():
    if head.direction != "down":  # Prevent moving opposite direction
        head.direction = "up"  # Set the direction to up

def go_down():
    if head.direction != "up":  # Prevent moving opposite direction
        head.direction = "down"  # Set the direction to down

def go_left():
    if head.direction != "right":  # Prevent moving opposite direction
        head.direction = "left"  # Set the direction to left

def go_right():
    if head.direction != "left":  # Prevent moving opposite direction
        head.direction = "right"  # Set the direction to right

# Function to move the snake in the current direction
def move():
    if head.direction == "up":  # If the direction is up
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y + 20)  # Move the head 20 units upwards

    if head.direction == "down":  # If the direction is down
        y = head.ycor()  # Get the current y-coordinate of the head
        head.sety(y - 20)  # Move the head 20 units downwards

    if head.direction == "left":  # If the direction is left
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x - 20)  # Move the head 20 units to the left

    if head.direction == "right":  # If the direction is right
        x = head.xcor()  # Get the current x-coordinate of the head
        head.setx(x + 20)  # Move the head 20 units to the right

# Keyboard bindings to control the snake's direction
wn.listen()  # Start listening for keyboard inputs
wn.onkeypress(go_up, "w")  # Bind the 'w' key to move the snake up
wn.onkeypress(go_down, "s")  # Bind the 's' key to move the snake down
wn.onkeypress(go_left, "a")  # Bind the 'a' key to move the snake left
wn.onkeypress(go_right, "d")  # Bind the 'd' key to move the snake right

# Main game loop
while True:
    wn.update()  # Update the screen with the latest changes

    # Check for a collision with the border (wrap around the screen)
    if head.xcor() > 290:  # If the head goes beyond the right edge
        head.setx(-290)  # Wrap around to the left side
    elif head.xcor() < -290:  # If the head goes beyond the left edge
        head.setx(290)  # Wrap around to the right side

    if head.ycor() > 290:  # If the head goes beyond the top edge
        head.sety(-290)  # Wrap around to the bottom side
    elif head.ycor() < -290:  # If the head goes beyond the bottom edge
        head.sety(290)  # Wrap around to the top side

    # Check for a collision with the food
    if head.distance(food) < 20:  # If the head is close enough to the food
        # Move the food to a random spot
        x = random.randint(-290, 290)  # Generate a random x-coordinate
        y = random.randint(-290, 290)  # Generate a random y-coordinate
        food.goto(x, y)  # Move the food to the random coordinates

        # Add a new segment to the snake
        new_segment = turtle.Turtle()  # Create a new turtle for the body segment
        new_segment.speed(0)  # Set the speed of the segment to maximum (fastest)
        new_segment.shape("circle")  # Set the shape of the segment to a circle
        new_segment.color("green")  # Set the color of the segment to green
        new_segment.penup()  # Lift the pen so it doesn't draw lines
        segments.append(new_segment)  # Add the new segment to the list of segments

        # Shorten the delay (make the snake move faster)
        delay -= 0.001  # Reduce the delay slightly after each food eaten

        # Increase the score
        score += 1  # Increment the score by 1

        # Update high score if needed
        if score > high_score:  # If the current score exceeds the high score
            high_score = score  # Update the high score to the current score

        # Update the score display
        pen.clear()  # Clear the previous score
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))  # Write the new scores

    # Move the body segments in reverse order (from last to first)
    for index in range(len(segments) - 1, 0, -1):  # Loop through the segments in reverse
        x = segments[index - 1].xcor()  # Get the x-coordinate of the previous segment
        y = segments[index - 1].ycor()  # Get the y-coordinate of the previous segment
        segments[index].goto(x, y)  # Move the current segment to the previous segment's position

    # Move the first segment to where the head is
    if len(segments) > 0:  # If there are any segments
        x = head.xcor()  # Get the current position of the head
        y = head.ycor()  # Get the current position of the head
        segments[0].goto(x, y)  # Move the first segment to the head's position

    move()  # Move the snake based on the current direction

    # Check for collision with the body segments
    for segment in segments:  # Loop through all segments
        if segment.distance(head) < 20:  # If the head collides with any body segment
            time.sleep(1)  # Pause the game for 1 second

            head.goto(0, 0)  # Reset the head to the center of the screen
            head.direction = "stop"  # Stop the snake's movement

            # Hide all body segments off-screen
            for segment in segments:
                segment.goto(1000, 1000)  # Move each segment far off the screen
            segments.clear()  # Clear the segments list

            score = 0  # Reset the score

            # Update the score display
            pen.clear()  # Clear the previous score
           



 
 
 
 
 

 
