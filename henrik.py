import turtle

#size=40
def kantet(size=40):
    for n in range(1,6):
        turtle.forward(size)
        turtle.right(72)


def sol():
#    from turtle import *
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(100)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
