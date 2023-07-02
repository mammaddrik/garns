import numpy as np
from random import sample
from .solver import solve

#::::: Generate Game :::::
def gen_game(dif):
    "Game creation function"
    board = np.zeros((9,9), dtype=int)
    hint_board = np.zeros((9,9), dtype=int)
    board[0] = sample(range(1,10), 9)
    solve(board)
    board = board.flatten()
    hint_board = hint_board.flatten()
    for i in sample(range(81),dif):
        hint_board[i] = board[i]
        board[i] = 0
    board = np.reshape(board,(9,9))
    hint_board = np.reshape(hint_board,(9,9))
    disa_board = np.not_equal(board,0)
    return board, hint_board, disa_board