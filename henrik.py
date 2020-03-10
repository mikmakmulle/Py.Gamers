import turtle

#size=40
def kantet(size=40):
    for n in range(1,6):
        turtle.forward(size)
        turtle.right(72)


def sol():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(100)
        turtle.left(170)
        if abs(pos()) < 1:
            break
    turtle.end_fill()
