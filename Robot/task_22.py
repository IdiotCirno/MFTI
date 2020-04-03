#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    ends=0
    while ends<2:
        fill_cell()
        if wall_is_on_the_left():
            while not(wall_is_on_the_right()):
                move_right()
                fill_cell()
        elif wall_is_on_the_right():
            while not(wall_is_on_the_left()):
                move_left()
                fill_cell()
        if not(wall_is_beneath()):
            move_down()
        else:
            while not(wall_is_on_the_left()):
                move_left()
            ends=2
        #break
        


if __name__ == '__main__':
    run_tasks()
