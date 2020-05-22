import turtle
import time

turtle.speed('fastest')
def minkovski(l, n):
    if n==0:
        turtle.forward(l)      
        return
    for i in [90, -90, -90, 0, 90, 90, -90, 0]:
        minkovski(l/4, n-1)
        turtle.left(i)
'''
    minkovski(l/4, n-1)
    turtle.left(90)
    minkovski(l/4, n-1)
    turtle.left(-90)
    minkovski(l/4, n-1)
    turtle.left(-90)
    minkovski(l/4, n-1)
    turtle.left(0)
    minkovski(l/4, n-1)
    turtle.left(90)
    minkovski(l/4, n-1)
    turtle.left(90)
    minkovski(l/4, n-1)
    turtle.left(-90)
    minkovski(l/4, n-1)
'''
    
    
for i in range(4):
    minkovski(300, 2)
    turtle.right(90)
