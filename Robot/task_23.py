#!/usr/bin/python3

from pyrob.api import *

def move_upd_down():
    while not(wall_is_above()):
        move_up()
        fill_cell()
    else:
        while not(wall_is_beneath()):
            move_down()

@task(delay=0.01)
def task_6_6():
    steps = 1
    move_right()
    while not(wall_is_on_the_right()):
        move_upd_down()
        move_right()
        steps += 1
    else:
        move_upd_down()
    move_left(steps)

if __name__ == '__main__':
    run_tasks()
