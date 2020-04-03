#!/usr/bin/python3

from pyrob.api import *

def plus():
    move_down()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    if wall_is_on_the_right():
        last=True
    else:
        last=False
    move_down()
    move_left()
    fill_cell()
    for i in range(2):
        move_up()
        fill_cell()
    move_left()
    return last


@task(delay=0.02)
def task_2_4():
    check=1
    while check:
        while not(plus()):
            move_right(4)
        
        while not(wall_is_on_the_left()):
            move_left()
        
        move_down(2)
        if not(wall_is_beneath()):
            move_down(2)
        else:
            move_up(2)
            check=0


if __name__ == '__main__':
    run_tasks()
