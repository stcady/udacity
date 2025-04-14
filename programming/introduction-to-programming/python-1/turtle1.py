import turtle
fred = turtle.Turtle()
fred.color("green")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

def draw_square():
    for i in range(4):
        jack.forward(100)
        jack.right(90)

for square in range(10):
    jack = turtle.Turtle()
    jack.color("red")
    jack.speed(0)
    draw_square()
    jack.penup()
    jack.forward(5)
    jack.left(5)
    jack.pendown()