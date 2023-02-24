#!/usr/bin/env python
#      _____ 
#     / ____|
#    | |  __  __ _ _ __ _ __  ___ 
#    | | |_ |/ _` | '__| '_ \/ __|
#    | |__| | (_| | |  | | | \__ \
#     \_____|\__,_|_|  |_| |_|___/
#
#    A sudoku solver & sudoku game   
#         Github: mammaddrik           

#::::: Library :::::
from garns.library.clearscreen.clearscr import clearScr
from garns.library.banner.banner import Banner
from garns.library.slowprint.slowprint import slowprint
from garns.library.color.color import Color,color_banner

#::::: Default Library :::::
from datetime import datetime
import webbrowser
import os
import sys
import time

try:
    clearScr()
    print(Banner.garns_banner)
    choice = input("garns@sudoku:~$ ")

    #::::: Sudoku File :::::
    if (choice == "01" or choice == "1"):
        clearScr()
        print(Banner.board_banner)
        board = []
        pwfile = input("Enter the file name: ")
        try:
            with open(pwfile) as f:
                for text in f:
                    text = text.strip('\n')
                    start = text.find("[")
                    end = text.find("]")
                    text = text[start + 1:end]
                    board.append([int(i) for i in text.split(',')])
                if board == pwfile:
                    sys.exit()
        except FileNotFoundError:
            slowprint(Color.BRed +"File Not Found.")
            sys.exit()
    
    #::::: Sudoku Manual :::::    
    elif (choice == "02" or choice == "2"):
        clearScr()
        print(Banner.board_banner)
        board = []
        slowprint(Color.BYellow+"Zero indicates an empty cell."+Color.End)
        try:
            for i in range(9):
                f = list(map(int, input("Enter a value for each cell: ").split(" ")))
                if len(f) == 9:
                    board.append(f)
                    for i,n in enumerate(f):
                        if n > 9:
                            slowprint(Color.BRed+"The entered numbers are greater than 9."+Color.End)
                            sys.exit()
                        elif n < 0:
                            slowprint(Color.BRed+"The entered numbers are smaller than 0."+Color.End)
                            sys.exit()
                else:
                    slowprint(Color.BRed+"Out of range."+Color.End)
                    sys.exit()
        except ValueError:
            slowprint(Color.BRed+"Cell must be Integer."+Color.End)
            sys.exit()

    #::::: Github :::::
    elif (choice == "00" or choice == "0"):
        clearScr()
        time.sleep(0.4)
        print(Banner.github_banner)
        url = "https://github.com/mammaddrik"
        webbrowser.open(url)
        sys.exit()
    
    #::::: Exit :::::
    elif (choice == "99"):
        print("\nGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()

    else:
        slowprint(Color.BRed+"\nIt is wronge."+Color.End)
        sys.exit()
        
except KeyboardInterrupt:
    slowprint(Color.BRed +"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()
    sys.exit()

#::::: Print Board :::::
def print_board(bo):
    "Border printing function."
    print(color_banner[5]+"┌───────┬───────┬───────┐"+Color.End)
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(color_banner[5]+"├───────┼───────┼───────┤"+Color.End)
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(color_banner[5]+"│ "+Color.End, end="")
            if j == 0:
                print(color_banner[5]+"│ "+Color.End, end="")
            if j == 8:
                print(str(bo[i][j])+color_banner[5]+" │ "+Color.End)
            else:
                print(str(bo[i][j]) + " ", end="")
    print(color_banner[5]+"└───────┴───────┴───────┘"+Color.End)

#::::: Find Empty :::::
def find_empty(bo):
    "Function to find empty value."
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None  

#::::: Solve :::::
def solve(bo):
    "Sudoku solving function."
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

#::::: Valid :::::
def valid(bo, num, pos):
    "Answer validity function for Sudoku"
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

try:
    print_board(board)
    solve(board)
    print_board(board)
except KeyboardInterrupt:
    slowprint(Color.BRed +"Finishing up..."+Color.End)
    time.sleep(0.4)
    clearScr()