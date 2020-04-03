#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    done=False
    sequence=0
    while not(wall_is_on_the_right()) and sequence<3:
        if cell_is_filled():
            sequence+=1
        else:
            sequence=0
        move_right()
    if sequence==3:
        move_left()

if __name__ == '__main__':
    run_tasks()
