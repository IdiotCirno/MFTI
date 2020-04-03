#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x=y=0
    l=1
    while not(wall_is_on_the_right()):
        move_right()
        l+=1
    move_left(l-1)
    for i in range(l):
        while not(wall_is_on_the_right()):
            move_right()
            x+=1
            if x!=y and x+y!=l-1:
                fill_cell()
            
        else:
            move_left(x)
            x=0
            if x!=y and x+y!=l-1:
                fill_cell()
        if y<l-1:
            move_down()
        y+=1



if __name__ == '__main__':
    run_tasks()
