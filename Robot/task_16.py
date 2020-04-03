#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    if not(wall_is_above()):
        while not(wall_is_above()):
            move_up()
    else:
        while not(wall_is_beneath()):
            move_down()
    
    if not(wall_is_on_the_left()):
        while not(wall_is_on_the_left()):
            move_left()
    else:
        while not(wall_is_on_the_right()):
            move_right()



if __name__ == '__main__':
    run_tasks()
