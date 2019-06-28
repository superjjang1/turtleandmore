from turtle import *

def drawsquare():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    mainloop()

def drawcircle():
    circle(180)

def drawhexagon():
    for i in range(6):
        forward(100)
        right(60)

def drawoctagon():
    for i in range(8):
        forward(200)
        right(45)

def drawpentagon():
    for i in range(5):
        forward(100)
        right(72)

def drawstar():
    for i in range(5):
        forward(100)
        right(144)

def drawtriangle():
    for i in range(3):
        forward(100)
        right(120)



