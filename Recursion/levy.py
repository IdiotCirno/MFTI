import turtle
import time

turtle.speed('fastest')
def levy(l, n):
    if n==0:
        turtle.forward(l)      
        return
    #for i in [90, -90, -90, 0, 90, 90, -90, 0]:
    turtle.left(45)
    levy((l*l/2)**0.5, n-1)
    turtle.right(90)
    levy((l*l/2)**0.5, n-1)
    turtle.left(45)

for i in range(4):
    levy(200, 6)
    turtle.right(90)
