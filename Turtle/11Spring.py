import turtle
import math

turtle.shape('turtle')
turtle.speed(9)
#turtle.penup()
turtle.goto(300,0)
turtle.goto(-300,0)
turtle.pendown()
turtle.left(90)
faces=40
radius=50



def spring(turtle, faces, radius):
    len=2*radius*math.sin(math.pi/faces)
    angle=360/faces
    for i in range(0,int(faces/2)+1):
        turtle.forward(len)
        turtle.right(angle)
    #turtle.left(angle)
'''    
    for i in range(0,int(faces/2)+1):
        turtle.forward(int(len*0.2))
        turtle.right(angle)
    turtle.left(angle)
'''

for i in range(1,21):
    spring(turtle, faces, radius)   
    turtle.setheading(-90)
    spring(turtle, int(faces/2), int(radius/4))
    turtle.setheading(90)
