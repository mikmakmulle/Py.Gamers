# Importer alle functioner i filen, direkte (uden at skulle skrive filnavn.funlktion

from andreas import *  # Hent Andreas funktioenr
from jonas   import *  # Hent Jonas funktioenr
from alvin   import *  # Hent Alvins funktioenr
from harald  import *  # Hent Haralds funktioenr
from henrik  import *  # Hent Henriks funktioenr
from martin  import *  # Hent Martins funktioenr
from simon   import *  # Hent Simons funktioenr
from loui   import * # hent Louis funktioner
from Jesper import * # hent Jesper funktioner

import turtle # her importerer vi hele turtle modulet

turtle.speed("fastest")
#turtle.color(0.4,0,1)
#turtle.pensize(4)


<<<<<<< HEAD

def hus(size=0):
  

=======
  turtle.pencolor("red")
  def hus(size=500):
  h = size/:2
>>>>>>> 782ab59de3605e545fb4df5d90e90800fe49fd65
  
  move(-200,200)
  firkant(250)
  move(50,50)
  trekant(250)
  move(500,0)
  firkant(100)
  move(40,0)
  firkant(100)
  move(-100)
  rektangel(200,100)
  
  

hus()

input()

