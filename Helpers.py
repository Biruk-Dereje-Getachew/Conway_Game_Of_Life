class Helpers:

    def __init__(self):
        pass

    def rectangle(self, turtle, width, height, location=[], heading=0):
        turtle.penup()
        turtle.goto(location) if location else 0
        turtle.pendown()
        turtle.setheading(heading)

        for _ in range(2):
            turtle.forward(width)
            turtle.right(45)
            turtle.forward(height)
            turtle.right(45)