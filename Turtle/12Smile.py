import turtle
import math
import time

def spring(turtle, faces, radius):
    len=2*radius*math.sin(math.pi/faces)
    angle=360/faces
    for i in range(0,int(faces/2)+1):
        turtle.forward(len)
        turtle.right(angle)

def circle(turtle, faces, radius):
    len=2*radius*math.sin(math.pi/faces)
    angle=360/faces
    for i in range(0,faces):
        turtle.forward(len)
        turtle.left(angle)

def moveturtle(turtle,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()  

turtle.shape('turtle')
turtle.speed(9)
faces=40
radius=50

#Head
turtle.begin_fill()
circle(turtle, faces*3, radius*4)
turtle.color('yellow')  
turtle.end_fill() 
turtle.color('black')

#Eyes
moveturtle(turtle,-100,200)
turtle.begin_fill()
circle(turtle, faces, radius)
turtle.color('blue')  
turtle.end_fill() 
turtle.color('black')

moveturtle(turtle,100,200)
turtle.begin_fill()
circle(turtle, faces, radius)
turtle.color('blue')  
turtle.end_fill() 
turtle.color('black')

#Nose
moveturtle(turtle,0,200)
turtle.width(20)
turtle.right(90)
turtle.forward(80)

#Mouth
moveturtle(turtle,50,100)
#turtle.right(90)
turtle.color('red')
spring(turtle, faces, radius)

time.sleep(2)