import turtle
import math

turtle.shape('turtle')
turtle.speed(9)
turtle.left(90)
faces=60
radius=100



def circle(turtle, faces, radius, turn):
    len=2*radius*math.sin(math.pi/faces)
    angle=360/faces
    for i in range(0,faces):
        turtle.forward(len)
        if turn=='left':
            turtle.left(angle)
        else:
            turtle.right(angle)



for i in range(1,21):
    if i%2:
        circle(turtle, faces, radius, 'left')
    else:
        circle(turtle, faces, radius, 'right')
    radius+=int(radius*0.05)
    faces+=int(faces*0.05)