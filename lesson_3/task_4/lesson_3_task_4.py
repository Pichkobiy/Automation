import turtle
square = turtle.Turtle()
square.shape("turtle")
square.color('blue','purple')
square.begin_fill()
for j in range (5):
    square.left(30)
    for i in range(4):
        square.forward(150)
        square.right(90)
square.end_fill()        
turtle.exitonclick()