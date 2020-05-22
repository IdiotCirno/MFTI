import turtle
import time

turtle.speed('fastest')

    
def dragon(l, n, side):
    if n==0:
        turtle.forward(l)
        return
    dragon((l*l/2)**0.5, n-1, 1)
    turtle.right(side * -90)
    dragon((l*l/2)**0.5, n-1, -1)


dragon(300, 10, 1)

'''

Tracing an iteration of the Heighway dragon curve from one end to the other, one encounters a series of 90-degree turns,
some to the right and some to the left. For the first few iterations the sequence of right (R) and left (L) turns is as follows:

    1st iteration: R
    2nd iteration: R R L
    3rd iteration: R R L R R L L
    4th iteration: R R L R R L L R R R L L R L L.

1. Add a right turn to the string
2. Take the original string and flip it backward (first character last, last first)
3. Take the flipped version and switch all the rights to lefts and the lefts to rights
4. Add the flipped version to the new string we made in the first step

def rl(n):
    s = ['r']
    for i in range(n-1):
        s += ['r'] + ['r' if i == 'l' else 'l' for i in s[::-1]]
    return s

'''