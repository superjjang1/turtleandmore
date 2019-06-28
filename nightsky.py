from turtle import *
from random import *
#night sky
setup(width=1000, height=900)
speed(0)
bgcolor("blue")
def drawstar(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    if fill:
        end_fill()
#above is code to draw the star
numstar = 0
while numstar < 20:
    x = randint(-200,700) #random x coordinate
    y = randint(-200, 700) #random y coordinate
    drawstar(5, True, "white") #calls the function
    penup() #moves the pen after it's been drawn
    goto(x, y)
    pendown() #places pen
    numstar = numstar + 1
while numstar < 50:
    x = randint(-200,700) #random x coordinate
    y = randint(-200, 700) #random y coordinate
    drawstar(25, True, "white") #calls the function
    penup() #moves the pen after it's been drawn
    goto(x, y)
    pendown() #places pen
    numstar = numstar + 1


mainloop()