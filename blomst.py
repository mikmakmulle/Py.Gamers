# Importer alle functioner i filen, direkte (uden at skulle skrive filnavn.funlktion
from andreas import *  # Hent Andreas funktioenr
from jonas   import *  # Hent Jonas funktioenr
from alvin   import *  # Hent Alvins funktioenr
from harald  import *  # Hent Haralds funktioenr
from henrik  import *  # Hent Henriks funktioenr
from martin  import *  # Hent Martins funktioenr
from simon   import *  # Hent Simons funktioenr

import turtle # her importerer vi hele turtle modulet

turtle.speed("fastest")
#turtle.color(0.4,0,1)
#turtle.pensize(4)

def flower():
  for n in range(1,11):
    turtle.pencolor("blue")
    circle(50)
    firkant(50)
    ottekant(50)
    trekant(50)
    sekskant(50)
    turtle.left(36)
    turtle.pencolor("green")
    circle(50)
    firkant(50)
    ottekant(50)
    trekant(50)
    sekskant(50)
    turtle.left(36)

flower()

input()
