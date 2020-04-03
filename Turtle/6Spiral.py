import turtle
from math import cos, sin, pi
import time

turtle.shape('turtle')

cnt = 200

f = 10 #угол

for i in range(0,cnt):
    p = i/(2*f)*pi
    x = p*cos(p)
    y = p*sin(p)
    turtle.goto(x, y)

#Where a controls the initial angle of the spiral, and b controls the distance between turnings
def spiral(turtle, rotations=6, a=0.0, b=5):
    theta = 0.0

    while theta < rotations * 2 * pi:
        radius = a + b * theta
        x, y = radius * cos(theta), radius * sin(theta)
        turtle.goto(x, y)
        theta += 0.1

spiral(turtle, 10, 0.0, 10)
'''
k=5 #смещение точки M по лучу r, при повороте на угол равный одному радиану
f=90 #угол?
p=k*f
cnt=80
step=5
t=5


for i in range(0,cnt):
    turtle.forward(k)
    turtle.left(f)
    k+=p
'''


'''
#WHAT THE FUCK
turtle.shape('turtle')
turtle.speed(9)
turtle.left(90)
faces=60
radius=100



def circle(turtle, faces, radius):
    len=2*radius*math.sin(math.pi/faces)
    angle=360/faces
    for i in range(0,int(faces/2)):
        turtle.forward(len)
        turtle.left(angle)




for i in range(1,21):
    if i%2:
        circle(turtle, faces, radius)
    else:
        circle(turtle, faces, radius)
    radius+=int(radius*0.05)
    faces+=int(faces*0.05)
'''