#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    direction=1
    move_right()
    for i in range(12):
        if direction>0:
            while not(wall_is_on_the_right()):
                fill_cell()
                move_right()
            else:
                move_down()
                move_left()
                direction=-1
        else:
            while not(wall_is_on_the_left()):
                fill_cell()
                move_left()
            else:
                move_down()
                move_right()
                direction=1


if __name__ == '__main__':
    run_tasks()
