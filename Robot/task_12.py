#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while not(wall_is_on_the_right()):
        if not(wall_is_above()) and wall_is_beneath():
            fill_cell()
        move_right()
    else:
        if not(wall_is_above()) and wall_is_beneath():
            fill_cell()


if __name__ == '__main__':
    run_tasks()
