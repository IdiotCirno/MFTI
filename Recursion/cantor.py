import turtle
import time

turtle.speed('fastest')
turtle.pensize(2)
turtle.penup()
turtle.setx(-300)
turtle.pendown()
def cantor(l, n):
    if n==0:
        turtle.forward(l)      
        return
    cantor(l/3, n-1)
    turtle.penup()
    cantor(l/3, 0)
    turtle.pendown()
    cantor(l/3, n-1)

for i in range(1, 10):
    cantor(600, i)
    turtle.penup()
    turtle.sety(i*5)
    turtle.left(180)
    turtle.pendown()
