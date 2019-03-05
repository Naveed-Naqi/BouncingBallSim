# Naveed Naqi
# July 29th 2018
# Bouncing ball simualtor

import turtle;
import random;

# Initial window set up

wn = turtle.Screen();
wn.screensize(1000, 1000);
wn.bgcolor("black");
wn.title("Bouncing Ball Simulator");
wn.screensize(600, 600);                                # Alters screen size
turtle.setup(600, 600);                                 # Alters the drawing window
wn.tracer(0);                                           # Turns off screen updating

balls = [];

colors = ["blue", "green", "yellow", "orange", "white", "purple"]

shapes = ["circle", "square", "triangle"]

for i in range(20):                                     # Creates the turtles
    balls.append(turtle.Turtle());

# Attributes and position of the ball

for ball in balls:
    ball.shape(random.choice(shapes));
    ball.color(random.choice(colors));
    ball.penup();
    ball.speed(0);
    randomXSpawn = random.randint(-200, 200);
    randomYSpawn = random.randint(-200, 200);
    ball.goto(randomXSpawn, randomYSpawn);
    ball.dy = 0;                                        # Vertical ball speed
    ball.dx = random.randint(-3, 3);                    # Each ball will travel at a different speed and direction
    ball.dr = random.randint(-5, 5);                    # Rotation of the ball

gravity = 0.1;

# This loop will go on forever  

while True:     
    wn.update();                                        # Will redraw the screen

    for ball in balls:
        ball.rt(ball.dr);
        ball.dy -= gravity;
        ball.sety(ball.ycor() + ball.dy);

        ball.setx(ball.xcor() + ball.dx);

        # Checks for a bounce

        if ball.ycor() < -300:
            ball.dy *= -1;
            ball.dr *= -1;
            ball.sety(-300);                            # Fixes gltich of ball getting stuck and the floor

        # Checks for a wall collision

        if ball.xcor() > 300:
            ball.dx *= -1;
            ball.dr *= -1;

        if ball.xcor() < -300:
            ball.dx *= -1;
            ball.dr *= -1;                              #Rotation of the ball reverses when it bounces against something

        

    








