#::::: Library :::::
from garns.library.color.color import Color,color_banner

class Banner:
    "A Class To Print Different Banners."
    #::::: Garns :::::
    garns_banner = (color_banner[0] + r"""      _____ 
     / ____|
    | |  __  __ _ _ __ _ __  ___ 
    | | |_ |/ _` | '__| '_ \/ __|
    | |__| | (_| | |  | | | \__ \
     \_____|\__,_|_|  |_| |_|___/""" + Color.End + """\n
  [01]Sudoku File   [02]Sudoku Manual
  [00]Github        [99]Exit\n""")
    
    #::::: board :::::
    board_banner = (color_banner[1] + r"""      _____ 
     / ____|
    | |  __  __ _ _ __ _ __  ___ 
    | | |_ |/ _` | '__| '_ \/ __|
    | |__| | (_| | |  | | | \__ \
     \_____|\__,_|_|  |_| |_|___/""" + Color.End+"\n")
    
    #::::: Github  :::::
    github_banner = (color_banner[2]+"""╔══════════════════════════════════════╗
║   \033[1;37m["""+color_banner[3]+"""+\033[1;37m]garns."""+color_banner[2]+"""                          ║
║   \033[1;37m["""+color_banner[4]+"""+\033[1;37m]A sudoku solver and sudoku game."""+color_banner[2]+"""║
╚══════════════════════════════════════╝"""+Color.End)