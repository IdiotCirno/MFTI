import turtle
import math

turtle.shape('turtle')

cnt=20
a=100
t=360/cnt


for i in range(0,cnt):
    turtle.forward(a)
    turtle.stamp()
    turtle.back(a)
    turtle.left(t)
