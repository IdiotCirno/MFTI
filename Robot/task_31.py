#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    direction=0 #0 - left 1 - right
    done=0
    while done<2:
        if direction:
            while wall_is_beneath():
                move_right()
                if wall_is_on_the_right():
                    direction=0
                    done+=1
                    break
            else:
                move_down()
                done=0
        else:
            while wall_is_beneath():
                move_left()
                if wall_is_on_the_left():
                    direction=1
                    done+=1
                    break
            else:
                move_down()
                done=0
    while not(wall_is_on_the_left()):
        move_left()
if __name__ == '__main__':
    run_tasks()
