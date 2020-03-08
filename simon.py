#Simon Fil !! nallerne væk!!

import turtle

def move(x=0,y=0):
  turtle.penup()
  if x > 0:
    turtle.forward(x)
  elif x < 0:
    turtle.backward(-x)

  if y > 0:
    turtle.right(90)
    turtle.forward(y)
    turtle.left(90)
  elif y < 0:  
    turtle.left(90)
    turtle.forward(-y)
    turtle.right(90)

  turtle.pendown()


