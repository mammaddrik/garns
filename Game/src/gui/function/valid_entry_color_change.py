from src.gui.style.entry_color_change import fg_to_red, fg_to_blue

#::::: Cell Selection :::::
def is_valid(entry,hint_board_val):
    "Cell Selection"
    if int(hint_board_val) != 0:
        VALUE = entry.get()
        if VALUE != "":
            if int(VALUE) != int(hint_board_val):
                fg_to_red(entry)
            if int(VALUE) == int(hint_board_val):
                fg_to_blue(entry)