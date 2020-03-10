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
turtle.color("red" , "blue")
#turtle.color(0.4,0,1)
#turtle.pensize(4)



def hus(size=500):
  h = size/2

  # Kasse
  move(-200,-200)
  firkant(250)
  
  # Tag
  move(-25,250)
  trekant(300)
  
  # Vinduer
  move(50,-150)
  turtle.begin_fill()
  firkant(40)
  move(150,0)
  firkant(40)
  turtle.end_fill()

  # Dør
  move(-75,-100)
  turtle.begin_fill()
  rektangel(100,50)
  turtle.end_fill()
  
 

hus()

input()

