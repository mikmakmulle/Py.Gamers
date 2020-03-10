#Simon Fil !! nallerne væk!!

import turtle

def move(x=0,y=0):
  turtle.setheading(90)
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


if __name__ == '__main__':
  size = 50
  for n in range(1,5):
    turtle.forward(size)
    turtle.left(90)

  move(290,290)  
  
  for n in range(1,5):
    turtle.forward(size)
    turtle.left(90)

