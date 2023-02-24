from .RCB_position import get_RCB_pos
from src.gui.style.entry_color_change import (
    bg_to_blue, 
    readonly_bg_to_blue,
    bg_to_lightblue,
    readonly_bg_to_lightblue,
    bg_to_white,
    readonly_to_white,
    bg_to_red,
    bg_to_green,
    fg_to_blue,
    reset_fg_to_black,
    fg_to_red,
    fg_to_white,
    board_fg_to_blue
)

#::::: Change Color :::::
def change_RCB_color(entry_list,readonly_board,x,y):
    "Choose the colors of each cell."
    _POS = get_RCB_pos(x,y)
    for i in range(len(_POS)):
        POS = _POS.pop()
        if readonly_board[POS[0]][POS[1]]:
            readonly_bg_to_lightblue(entry_list[POS[0]][POS[1]])
        else:
            bg_to_lightblue(entry_list[POS[0]][POS[1]])
    if readonly_board[x][y]:
        readonly_bg_to_blue(entry_list[x][y])
    else:
        bg_to_blue(entry_list[x][y]) 

#::::: Reset Color :::::
def reset_RCB_color(entry_list,readonly_board,x,y):
    "Choose the colors of each cell."
    _POS = get_RCB_pos(x,y)
    for i in range(len(_POS)):
        POS = _POS.pop()
        if readonly_board[POS[0]][POS[1]]:
            readonly_to_white(entry_list[POS[0]][POS[1]])
        else:
            bg_to_white(entry_list[POS[0]][POS[1]])