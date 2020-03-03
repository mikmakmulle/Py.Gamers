# Master

# Importer alle functioner i filen, direkte (uden at skulle skrive filnavn.funlktion


import andreas   # Hent Andreas funktioenr
import jonas     # Hent Jonas funktioenr
import harald    # Hent Haralds funktioenr
import henrik    # Hent Henriks funktioenr
import martin    # Hent Jonas funktioenr
import simon     # Hent Jonas funktioenr

import turtle # her importerer vi hele turtle modulet

#turtle.speed("fastest")
#turtle.color(0.4,0,1)
#turtle.pensize(4)

def move(x=0,y=0):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

def flower():
  for n in range(1,11):
    circle(50)
    turtle.left(36)




input()
