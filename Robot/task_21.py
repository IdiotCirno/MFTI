#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    while not(wall_is_beneath()):

        while not(wall_is_beneath() or wall_is_on_the_right()):
            if wall_is_on_the_left():
                move_right()
                move_down()
            fill_cell()            
            move_down()
            if not(wall_is_beneath()):
                move_right()
        move_left()
        if (wall_is_beneath() and wall_is_on_the_left()):
            move_right()
            break
        else:
            move_right()
        while not(wall_is_on_the_left()):
            if wall_is_beneath():
                move_left()
                move_up()
            fill_cell()            
            move_left()
            if not(wall_is_on_the_left()):
                move_up()
        

if __name__ == '__main__':
    run_tasks()
'''
    move_right()
    move_down()
    while not(wall_is_beneath()):

        while not(wall_is_beneath() or wall_is_on_the_right()):
            fill_cell()
            print(1)
            move_right()
            print(2)
            move_down()
            print(3)
        else:
            move_left(2)
            move_up()
        #print(1.5)
        while not(wall_is_on_the_left()):
            fill_cell()
            move_left()
            move_up()
            #print(2)
        else:
            move_right()
            move_down(2)
        
        #print(2.5)
        
'''