#!/usr/bin/env python
#
#   _________         .___      __          
#  /   _____/__ __  __| _/____ |  | ____ __ 
#  \_____  \|  |  \/ __ |/  _ \|  |/ /  |  \
#  /        \  |  / /_/ (  <_> )    <|  |  /
# /_______  /____/\____ |\____/|__|_ \____/ 
#         \/           \/           \/      
#        A sudoku solver & sudoku game   
#              Github: mammaddrik    

# ::::: Default Library :::::
import tkinter as tk

#::::: Library :::::
from src.gui.sudoku_gui import GUI

def main():
    "Main function"
    root = tk.Tk()
    root.geometry("770x490")
    root.configure(background='#142f43')
    root.title("Garns")
    Game = GUI(root)
    Game.generate_sudoku_board()
    Game.right_side_option_block()
    root.mainloop()

if __name__ == '__main__':
    main()