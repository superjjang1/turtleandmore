from turtle import *
#size fill color

def drawsquare(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    if fill:
        end_fill()


def drawcircle(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    circle(size)
    if fill:
        end_fill()

def drawhexagon(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(6):
        forward(size)
        right(60)
    if fill:
        end_fill()

def drawoctagon(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(8):
        forward(size)
        right(45)
    if fill:
        end_fill()

def drawpentagon(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(5):
        forward(size)
        right(72)
    if fill:
        end_fill()

def drawstar(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(5):
        forward(100)
        right(144)
    if fill:
        end_fill()

def drawtriangle(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(3):
        forward(size)
        right(120)
    if fill:
        end_fill()



mainloop()