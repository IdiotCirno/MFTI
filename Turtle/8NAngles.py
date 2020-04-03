import turtle
from math import cos, sin, pi
import time

#R = a/2sin(360/2n)
def nAngle(turtle, n, R, step):
    f = 360/n
    a = R * 2 * (sin(pi/n))
    turtle.left(90)
    turtle.left(f*0.5)
    for i in range(1,n+1):
        turtle.forward(a)
        turtle.left(f)
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
    R += step
    return(R)



cnt = 11
R = 50
step = 40
turtle.shape('turtle')
turtle.speed(10)

for i in range(3,cnt+3):    
    R = nAngle(turtle, i, R, step)