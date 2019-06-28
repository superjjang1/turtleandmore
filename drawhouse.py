from turtle import *
bgcolor("green")

def drawsquare(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    if fill:
        end_fill()

def drawrectangle(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    if fill:
        end_fill()    
def drawtriangle(size, fill, mycolor):
    color(mycolor)
    if fill:
        begin_fill()
    for i in range(3):
        right(120)
        forward(size)
        right(120)
    if fill:
        end_fill()

drawrectangle(200, True, "black")
penup()
goto(-90,0)
pendown()
drawrectangle(200,True,"White")
penup()
goto(-180,0)
drawrectangle(200,True,"Blue")
penup()
goto(0,320)
pendown()
drawtriangle(380, True, "black")


mainloop()