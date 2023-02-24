import tkinter as tk
import numpy as np

from .style._style import STYLE
from .style.entry_color_change import board_fg_to_blue

from .function.only_digit import ONLY_DIGIT
from .function.RCB_color_change import change_RCB_color, reset_RCB_color
from .function.generate_game import gen_game
from .function.entry_operations import (
    update_board, 
    format_value,
    insert_value,
    delete_value, 
    restart_board, 
    clear_all_board,
    collect_entry_values)
from .function.valid_entry_color_change import is_valid
from .function.speed_visual_solve import stop_solving, setup_visual_solve, speed_visual_solve

class GUI(STYLE):
    def __init__(self, _master):
        super().__init__()
        self._master = _master
        self.Entry_list = [[" " for i in range(9)] for j in range(9)]
        self.Game_board = None
        self.Readonly_board = np.zeros((9,9), dtype=int)
        self.Hint_board = None
        self.Entry_Queue = []
        self.c_pos_x = None
        self.c_pos_y = None
        self.is_clear = True
        self.visual_running = False
        self.only_digit = self._master.register(ONLY_DIGIT)
        self.running = False
        
    def start_running(self):
        self.running = True

    def stop_running(self):
        self.running = False
    
    def update_current_position(self, x, y):
        self.c_pos_x = x
        self.c_pos_y = y

    def generate_sudoku_board(self):
        Board_frame = tk.Frame(self._master)
        Board_frame.grid(row=0, column=0, padx=15, pady=15)
        p = 0
        for i in range(9):
            q = 0
            for j in range(9):
                if (p+1) % 4 == 0 and p != 0:
                    l1 = tk.Canvas(Board_frame,width=1,height=1,bg="white")
                    l1.grid(row=p, column=q)
                    p += 1
                if (q+1) % 4 == 0 and q != 0:
                    l1 = tk.Canvas(Board_frame,width=1,height=1,bg="white")
                    l1.grid(row=p, column=q)
                    q += 1
                entry = tk.Entry(
                    Board_frame,
                    width=2,
                    font=("Helvetica", 30),
                    bg="white",
                    relief="ridge",
                    validate ="key",
                    validatecommand = (self.only_digit, '%P'))
                entry.grid(row=p, column=q)
                entry.bind("<Button-1>", lambda e=None, x=i, y=j: self.entry_on_left_click(x, y))
                entry.bind("<Button-3>", lambda e=None, x=i, y=j: self.entry_on_right_click(x, y))
                entry.insert(0, " ")
                q += 1
                self.Entry_list[i][j] = entry
            p += 1
            
    def right_side_option_block(self):
        right_block_frame = tk.Frame(self._master,bg="white")
        title_frame = tk.Frame(right_block_frame,bg="white")
        title = tk.Label(title_frame, 
            text=" GARNS ", 
            fg = self.Option_title["fg"],
            bg = self.Option_title["bg"],
            font = self.Option_title["font"]
            )
        title.grid(row=0,column=0)
        title_frame.grid(row=0,column=0)
        option_frame = tk.Frame(right_block_frame,bg="white")
        
        #::::: NEW Game :::::
        new_game_label_frame = tk.LabelFrame(option_frame,text="  NEW GAME ")
        self.Option_Frame_Add_Style(new_game_label_frame)
        easy_game = tk.Button(new_game_label_frame, text = "Easy", command= lambda : self.easy_hard_game_button_action(41))
        self.Option_Button_Add_Style(easy_game)
        easy_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        hard_game = tk.Button(new_game_label_frame, text = "Hard", command= lambda : self.easy_hard_game_button_action(56))
        self.Option_Button_Add_Style(hard_game)
        hard_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        new_game_label_frame.grid(row=0, column=0, pady=self.Option_Frame_pady)

        #::::: CLEAR :::::
        clear_label_frame = tk.LabelFrame(option_frame, text="  CLEAR  ")
        self.Option_Frame_Add_Style(clear_label_frame)
        restart_game = tk.Button(clear_label_frame, text="Restart", command=self.restart_button_action)
        self.Option_Button_Add_Style(restart_game)
        restart_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        clear_all_game = tk.Button(clear_label_frame, text = "Clear All", command=self.clear_all_button_action)
        self.Option_Button_Add_Style(clear_all_game)
        clear_all_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        clear_label_frame.grid(row=1, column=0, pady=self.Option_Frame_pady)

        #::::: Solve :::::
        solve_label_frame = tk.LabelFrame(option_frame, text="  SOLVE  ")
        self.Option_Frame_Add_Style(solve_label_frame)
        visual_game = tk.Button(solve_label_frame, text="Visual", command=lambda : self.speed_visual_solve_button_action(True))
        self.Option_Button_Add_Style(visual_game)
        visual_game.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        speed_game = tk.Button(solve_label_frame, text = "Speed", command=lambda : self.speed_visual_solve_button_action(False))
        self.Option_Button_Add_Style(speed_game)
        speed_game.grid(row=0,column=1, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        solve_label_frame.grid(row=3, column=0, pady=self.Option_Frame_pady)
        option_frame.grid(row=1, column=0)
        right_block_frame.grid(row=0, column=1, padx=10)     

        #::::: HELP :::::
        help_label_frame = tk.LabelFrame(option_frame, text="  HELP  ")
        self.Option_Frame_Add_Style(help_label_frame)
        hint_b = tk.Button(help_label_frame, text="Hint", command=self.hint_button_action)
        self.Option_Button_Add_Style(hint_b)
        hint_b.grid(row=0,column=0, padx=self.Option_Button_padx, pady=self.Option_Button_pady)
        help_label_frame.grid(row=4, column=0, pady=self.Option_Frame_pady)
         
    def entry_on_left_click(self,x,y):
        if not self.visual_running:
            self.add_to_entry_queue(x,y)
            self.update_current_position(x, y)
            if len(self.Entry_Queue) == 2:
                entry = self.Entry_list[self.Entry_Queue[0][0]][self.Entry_Queue[0][1]]
                format_value(entry)
                reset_RCB_color(self.Entry_list,self.Readonly_board,self.Entry_Queue[0][0],self.Entry_Queue[0][1])
                if self.Hint_board is not None:
                    is_valid(entry, self.Hint_board[self.Entry_Queue[0][0]][self.Entry_Queue[0][1]])
            change_RCB_color(self.Entry_list,self.Readonly_board,x,y)

    def entry_on_right_click(self,x,y):
        delete_value(self.Entry_list[x][y])
        
    def easy_hard_game_button_action(self,dif):
        if not self.running:
            self.Game_board,self.Hint_board,self.Readonly_board = gen_game(dif)
            update_board(self.Game_board, self.Entry_list)
            self.is_clear = False
            self.Entry_Queue.clear()

    def restart_button_action(self):
        stop_solving()
        restart_board(self.Game_board,self.Entry_list)
        
    def clear_all_button_action(self):
        stop_solving()
        clear_all_board(self.Game_board,self.Entry_list)
        self.Game_board = None
        self.Readonly_board = np.zeros((9,9), dtype=int)
        self.Hint_board = None
        self.is_clear = True
        self.Entry_Queue.clear()

    def speed_visual_solve_button_action(self, is_visual):
        if is_visual and self.running:
            return
        if is_visual:
            self.start_running()
        self.visual_running = True
        if self.is_clear:
            board = collect_entry_values(self.Entry_list)
            self.Game_board = board.copy()
        else:
            board = self.Game_board.copy()
        b = board.copy()
        setup_visual_solve(self._master, self.Entry_list, self.Hint_board, self.is_clear, is_visual)
        speed_visual_solve(board)
        if is_visual:
            board_fg_to_blue(self.Entry_list,b)
        del b,board
        self.visual_running = False
        if is_visual:
            self.stop_running()
            
    def get_c_pos(self):
        return self.c_pos_x, self.c_pos_y
    
    def add_to_entry_queue(self,x,y):
        if len(self.Entry_Queue) == 2:
            self.Entry_Queue.pop(0)
        self.Entry_Queue.append([x,y])
        
    def hint_button_action(self):
        if not self.is_clear:
            insert_value(self.Entry_list[self.c_pos_x][self.c_pos_y],self.Hint_board[self.c_pos_x][self.c_pos_y])