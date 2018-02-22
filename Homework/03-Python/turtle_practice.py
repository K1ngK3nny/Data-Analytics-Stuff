import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)


def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)


for i in range(36):
    square(100, 90)
    my_turtle.left(10)
