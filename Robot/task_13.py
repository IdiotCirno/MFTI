#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while True:
        if wall_is_beneath() and wall_is_above():
            pass
        elif wall_is_above():
            move_down()
            fill_cell()
            move_up()
        elif wall_is_beneath():
            move_up()
            fill_cell()
            move_down()
        elif not(wall_is_beneath()) and not(wall_is_above()):
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()
        if wall_is_on_the_right():
            break
        else:
            move_right()



if __name__ == '__main__':
    run_tasks()
