# Importer alle functioner i filen, direkte (uden at skulle skrive filnavn.funlktion

from andreas import *  # Hent Andreas funktioenr
from jonas   import *  # Hent Jonas funktioenr
from alvin   import *  # Hent Alvins funktioenr
from harald  import *  # Hent Haralds funktioenr
from henrik  import *  # Hent Henriks funktioenr
from martin  import *  # Hent Martins funktioenr
from simon   import *  # Hent Simons funktioenr
from loui   import * # hent Louis funktioner

import turtle # her importerer vi hele turtle modulet

turtle.speed("fastest")
#turtle.color(0.4,0,1)
#turtle.pensize(4)


  turtle.pencolor("red")
  def hus(size=500):
  h = size/:2
  
  move(-200,200)
  firkant(h)
  move(-h/10,-h)
  
  trekant(h * 1.2)
  move(h/8+h/10,h/2)
  turtle.begin_fill()
  firkant(h/6)
  move(h/1.8,0)
  firkant(h/6)
  turtle.end_fill()
  move(h/-3.5,40)
  turtle.begin_fill()
  rektangel(h)
  turtle.end_fill()
  

hus()

input()

