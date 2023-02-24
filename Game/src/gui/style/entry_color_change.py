#::::: Colors :::::
SELECT_COLOR = "#bbdefb"
HIGHLIGHT_COLOR = "#e2ebf3"
WHITE_COLOR = "white" 
BLACK_COLOR = "black"
FG_COLOR = "#2285e7"
RED_COLOR = "#9c0900"
LIGHTRED_COLOR = "#de6e67"
GREEN_COLOR = "#0e9924"

def bg_to_blue(entry):
    entry.config(bg = SELECT_COLOR)

def readonly_bg_to_blue(entry):
    entry.config(readonlybackground = SELECT_COLOR)

def bg_to_lightblue(entry):
    entry.config(bg = HIGHLIGHT_COLOR)

def readonly_bg_to_lightblue(entry):
    entry.config(readonlybackground = HIGHLIGHT_COLOR)

def bg_to_white(entry):
    entry.config(bg = WHITE_COLOR
    )

def readonly_to_white(entry):
    entry.config(readonlybackground = WHITE_COLOR)


def bg_to_red(entry):
    entry.config(bg = LIGHTRED_COLOR)

def bg_to_green(entry):
    entry.config(bg = GREEN_COLOR)

def fg_to_blue(entry):
    entry.config(fg = FG_COLOR)

def reset_fg_to_black(entry):
    entry.config(fg = BLACK_COLOR)

def fg_to_red(entry):
    entry.config(fg = RED_COLOR)

def fg_to_white(entry):
    entry.config(fg = WHITE_COLOR)

def board_fg_to_blue(entry_list, board):
    for i in range(9):
        for j in range(9):
            bg_to_white(entry_list[i][j])
            if board[i][j] == 0:
                fg_to_blue(entry_list[i][j])
            readonly_to_white(entry_list[i][j])