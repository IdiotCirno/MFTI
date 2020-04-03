#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    step=1
    wall=False
    while not(wall):
        for i in range(step+1):
            move_right()
            if wall_is_on_the_right():
                wall=True
                break
        if not(wall):
            fill_cell()
            step+=1


if __name__ == '__main__':
    run_tasks()
