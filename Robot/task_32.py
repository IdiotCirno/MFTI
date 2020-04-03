#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    filled=0
    while wall_is_beneath():
        if wall_is_above():
            fill_cell()
        else:
            while not(wall_is_above()):
                move_up()
                if not(cell_is_filled()):
                    fill_cell()
                else:
                    filled+=1
            else:
                while not(wall_is_beneath()):
                    move_down()
        move_right()
    mov('ax',filled)

if __name__ == '__main__':
    run_tasks()
