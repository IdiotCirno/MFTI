#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    direction=-1
    while wall_is_above():
        if not(wall_is_on_the_left()) and direction<0:
            move_left()
        elif wall_is_on_the_right():
            break
        else:
            direction=1
            move_right()
    else:
        while not(wall_is_above()):
            move_up()
        while not(wall_is_on_the_left()):
            move_left()


if __name__ == '__main__':
    run_tasks()
