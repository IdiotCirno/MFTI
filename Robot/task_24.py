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

@task
def task_2_1():
    move_right()
    move_down()
    plus()



if __name__ == '__main__':
    run_tasks()
