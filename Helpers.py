def square(turtle, color, width, location=[], heading=0):
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(location[0] * width, location[1] * width) if location else 0
    turtle.pendown()
    turtle.setheading(heading)

    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()