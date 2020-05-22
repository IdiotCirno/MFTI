import turtle
import time

turtle.speed('fastest')
def koch(l, n):
    if n==0:
        turtle.forward(l)      
        return
        #for i in range(3):
    koch(l/3, n-1)
    turtle.left(60)
    koch(l/3, n-1)
    turtle.right(120)
    koch(l/3, n-1)
    turtle.left(60)
    koch(l/3, n-1)

def kochSf(l, n):
    for i in range(3):
        koch(l, n)
        turtle.right(120)

    
    

kochSf(300, 4)
