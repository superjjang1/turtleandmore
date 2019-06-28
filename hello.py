# This is exercise 1
# def hello(name):
#     print("Hello ", name)
# hello("Sean")

#exercise 2
# import matplotlib.pyplot as plot 
# def f(x):
#     x = x + 1
#     return x

# xs = list(range(-3, 4))
# ys = []

# for x in xs:
#     ys.append(f(x))
# plot.plot(xs, ys)
# plot.show()

#exercise 3
# import matplotlib.pyplot as plot
# def f(x):
#     x = x * x
#     return x
# xs = list(range(-100, 100))
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)
# plot.show()

#exercise 4
# import matplotlib.pyplot as plot
# def f(x):
#     if x % 2 != 0:
#         return 1
#     elif x % 2 == 0:
#         return -1
# xs = list(range(-5, 5))
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.bar(xs,ys)   
# plot.show() 

#exercise 5
# import math
# import matplotlib.pyplot as plot
# def f(x):
#     return math.sin(x)
# xs = list(range(-5, 5))
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)   
# plot.show()

#exercise 6
# import numpy
# from numpy import arange 


# def f(x):
#     return math.sin(x)
# xs = arange(-5, 6, 0.1)
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs,ys)
# plot.show()
#exercise 7
# def f(x):
#     return 1.8 * x + 32
    
# xs = arange(32, 101, 1)
# ys = []
# for x in xs:
#     ys.append(x)
# plot.plot(xs,ys)
# plot.show()


#exercise 8 play again
# def intro():
#     print("Hello, we're going to play a game, what is your name?: ")
#     myname = input()
#     print ("Hi, "+ myname + ".")
# PlayAgain = 'y'
# while PlayAgain == 'y':
#     intro()
#     print('Do you want to play again? (y/n): ')
#     PlayAgain = input()

#exercise 9 play again again
def PlayAgain(answer):
    if answer == "Y":
        return True
    elif answer == "N":
        return False
    else:
        print("Invalid Input")
        return True
    
answer = "Y"
while PlayAgain(answer):
    answer = (input("Play Again? (Y/N): "))
    PlayAgain(answer)
