from turtle import Turtle, Screen


def forward():
    timmy.forward(10)


def backward():
    timmy.forward(-10)


def left():
    timmy.left(10)


def right():
    timmy.right(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


# Create object of Turtle and Screen class
timmy = Turtle()
screen = Screen()

# Move Forward
screen.onkey(key='w', fun=forward)
screen.onkeypress(key='Up', fun=forward)

# Move Backward
screen.onkey(key='s', fun=backward)
screen.onkeypress(key='Down', fun=backward)

# Turn Left
screen.onkey(key='a', fun=left)
screen.onkeypress(key='Left', fun=left)

# Turn Right
screen.onkey(key='d', fun=right)
screen.onkeypress(key='Right', fun=right)

# Clear the screen
screen.onkey(key='c', fun=clear)

screen.listen()
screen.exitonclick()
