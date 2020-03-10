import turtle
from loui   import *
from andreas import *

if __name__ == '__main__':
    def trekant(size=40):
        for n in range(1,4):
            turtle.forward(size)
            turtle.left(120)
            
def godblomst():
    circle (30)
    turtle.penup()
    turtle.goto(0,60)
    turtle.pendown()
    circle (75)
    turtle.penup()
    turtle.goto(-30,30)
    turtle.left(90)
    turtle.pendown()
    circle (75)
    turtle.penup()
    turtle.goto(0,0)
    turtle.left(90)
    turtle.pendown()
    circle (75)
    turtle.penup()
    turtle.goto(30,30)
    turtle.left(90)
    turtle.pendown()
    circle (75)