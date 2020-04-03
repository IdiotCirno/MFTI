#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled=0
    while filled<5:
        if cell_is_filled():
            filled+=1
        move_right()
    move_left()

if __name__ == '__main__':
    run_tasks()
