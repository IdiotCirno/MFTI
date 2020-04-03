import turtle
from math import cos, sin, pi
import time


def NStar(turtle, n, len):
    angle=180*(n-2)/n #угол n-угольника
    angle=angle+(180-angle)/2
    angle=90*(n-2)/n+90
    print(angle)
    for i in range(0,n):
        turtle.left(angle)
        turtle.forward(len)


turtle.shape('turtle')
turtle.speed(5)

len=100
n=11
NStar(turtle, n, len)
