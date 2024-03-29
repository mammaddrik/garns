from time import sleep

from .solver import solve, valid, find_empty
from .entry_operations import (
    insert_value,
    delete_value,
    update_values, 
    update_values)

from src.gui.style.entry_color_change import (
    bg_to_red,
    bg_to_green,
    fg_to_white
)

IS_CLEAR = None
IS_VISUAL = None
HINT_BOARD = None
ENTRY_LIST = None
MASTER = None
RUN = True

select_time = 0.00
green_time = 0.05
red_time = 0.04

#::::: Stop Solving :::::
def stop_solving():
    "The stop function solves."
    global RUN
    RUN = False

#::::: Visual Solver :::::
def setup_visual_solve(master,entry_list, hint_board, is_clear, is_visual):
    "Visual Solver function."
    global IS_CLEAR, IS_VISUAL, HINT_BOARD, ENTRY_LIST, MASTER, RUN
    IS_CLEAR = is_clear
    IS_VISUAL = is_visual
    HINT_BOARD = hint_board
    ENTRY_LIST = entry_list
    MASTER = master
    RUN = True

#::::: Speed Visual Solve :::::
def speed_visual_solve(board):
    "Visual Solver function."
    if not IS_VISUAL and IS_CLEAR:
        solve(board)
        update_values(board, ENTRY_LIST)
        return
    if not IS_VISUAL:
        update_values(HINT_BOARD, ENTRY_LIST)
    if IS_VISUAL:
        find = find_empty(board)
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if IS_VISUAL and RUN:
                bg_to_red(ENTRY_LIST[row][col])
                fg_to_white(ENTRY_LIST[row][col])
                delete_value(ENTRY_LIST[row][col])
                insert_value(ENTRY_LIST[row][col],i)
                MASTER.update()
                sleep(select_time)
            if valid(board, i, (row, col)):
                if IS_VISUAL and RUN:
                    bg_to_green(ENTRY_LIST[row][col])
                    delete_value(ENTRY_LIST[row][col])
                    insert_value(ENTRY_LIST[row][col],i)
                    MASTER.update()
                    sleep(green_time)
                board[row][col] = i
                if speed_visual_solve(board):
                    return True
                board[row][col] = 0
                if IS_VISUAL and RUN:
                    bg_to_red(ENTRY_LIST[row][col])
                    fg_to_white(ENTRY_LIST[row][col])
                    delete_value(ENTRY_LIST[row][col])
                    insert_value(ENTRY_LIST[row][col],0)
                    MASTER.update()
                    sleep(red_time)
        return False