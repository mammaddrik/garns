import re
import numpy as np
from src.gui.style.entry_color_change import (bg_to_white, readonly_to_white, fg_to_blue, reset_fg_to_black)

#::::: Read Only Mode :::::
def read_only_mode(entry):
    "Read-only mode function."
    entry.config(state = 'readonly', readonlybackground = 'white')

#::::: Normal Mode :::::
def normal_mode(entry):
    "Normal mode function."
    entry.config(state = 'normal')

#::::: Insert Value :::::
def insert_value(entry,n):
    "insert value in entry."
    entry.insert(0,f" {n}")

#::::: Delete Value :::::
def delete_value(entry):
    "Function to remove value from input."
    entry.delete(0, 'end')

#::::: Format Value :::::
def format_value(entry):
    "Format function."
    VALUE = entry.get()
    if re.match(r"(\d)",VALUE):
        delete_value(entry)
        insert_value(entry,VALUE)

#::::: Restart Board ::::::
def restart_board(board,entry_list):
    "Reset function."
    for i in range(9):
        for j in range(9):
            if board is None:
                 delete_value(entry_list[i][j])
            elif board[i][j] == 0:
                delete_value(entry_list[i][j])

#::::: Clear Board ::::::
def clear_all_board(board,entry_list):
    "Clear function."
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]
            if board is not None:
                if board[i][j] > 0:
                    normal_mode(entry)
            delete_value(entry)
            fg_to_blue(entry)
            bg_to_white(entry)

#::::: Update Board ::::::
def update_board(board,entry_list):
    "Function to update values."
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]
            normal_mode(entry)
            delete_value(entry)
            if board[i][j] > 0:
                insert_value(entry,board[i][j])
                read_only_mode(entry)
                readonly_to_white(entry)
                reset_fg_to_black(entry)
            else:
                fg_to_blue(entry)
                bg_to_white(entry)

#::::: Visual Solve :::::
def collect_entry_values(entry_list):
    "Visual solution function."
    board = np.zeros((9,9), dtype=int)
    for i in range(9):
        for j in range(9):
            format_value(entry_list[i][j])
            VALUE = entry_list[i][j].get()
            try:
                board[i][j] = int(VALUE)
            except: pass
    return board

#::::: Speed Solve :::::
def update_values(hint_board,entry_list):
    "Function to update values."
    for i in range(9):
        for j in range(9):
            entry = entry_list[i][j]
            if hint_board[i][j] > 0:
                delete_value(entry)
                insert_value(entry,hint_board[i][j])
                fg_to_blue(entry)
                bg_to_white(entry)