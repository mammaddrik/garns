import tkinter as tk
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