import turtle
from math import cos, sin, pi
import time

turtle.shape('turtle')

cnt = 20
a = 10
f = 90

for i in range(0,cnt):    
    for j in range(2):
        turtle.forward(a)
        turtle.left(f)
    a += 10