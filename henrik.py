import turtle

#size=40
def kantet(size=40):
    for n in range(1,6):
        turtle.forward(size)
        turtle.right(72)

<<<<<<< HEAD
    
def sol():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(100)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()


if __name__ == "__main__":

    sol()
=======
if __name__ == '__main__':
    kantet()
>>>>>>> 822c8d0d4f46c246f923bfb6183c8110ac58fa02
