import turtle
import math

turtle.shape('turtle')

n=360
R=100
a=2*R*math.sin(math.pi/n)
t=360/n

for i in range(0,n):
    turtle.forward(a)
    turtle.left(t)
