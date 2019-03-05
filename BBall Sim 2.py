# Naveed Naqi
# July 29th 2018
# Bouncing ball simualtor

import turtle

# Initial window set up

wn = turtle.Screen();
wn.screensize(1000, 1000);
wn.bgcolor("black");
wn.title("Bouncing Ball Simulator");
wn.tracer(0);                   #Turns off screen updating

# Attributes and position of the ball

ball = turtle.Turtle();
wn.screensize(600, 600);        # Alters screen size
turtle.setup(600, 600);         # Alters the drawing window
ball.shape("circle");
ball.color("green");
ball.penup();
ball.speed(0);
ball.goto(0, 200);
ball.dy = 0;                    # Vertical ball speed
ball.dx = 2;                    # Horizontal ball speed

gravity = 0.1;

# This loop will go on forever

while True:     
    wn.update();                # Will redraw the screen

    ball.dy -= gravity;
    ball.sety(ball.ycor() + ball.dy);

    ball.setx(ball.xcor() + ball.dx);

    # Checks for a bounce

    if ball.ycor() < -300:
        ball.dy *= -1;

    # Checks for a wall collision

    if ball.xcor() > 300:
        ball.dx *= -1;

    if ball.xcor() < -300:
        ball.dx *= -1;

        

    








