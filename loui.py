import turtle



def rektangel(height,width):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

if __name__ == "__main__":
    rektangel(250,25)
    turtle.left(90)
    turtle.forward(250)
    #turtle.