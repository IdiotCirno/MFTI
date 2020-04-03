#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not(cell_is_filled()):
        move_up()
    else:
        move_left()
        direction=-1
        while not(cell_is_filled()):
            if direction<0:
                direction=abs(direction)+1
                move_right(direction)
            else:
                direction=-(direction+1)
                move_left(abs(direction))
if __name__ == '__main__':
    run_tasks()
