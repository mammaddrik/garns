from .Option_block import Option_Style

class STYLE(Option_Style):
    def __init__(self):
        super().__init__()

    def Option_Button_Add_Style(self,Button) -> None:
        Button.config(
            width = self.Option_Button["width"],
            bg = self.Option_Button["bg_color"], 
            fg = self.Option_Button["font_color"], 
            relief = self.Option_Button["relief"], 
            activebackground = self.Option_Button["Active_bg_color"],
            activeforeground = self.Option_Button["Active_fg_color"],
            font = "bold")

        Button.bind("<Enter>",  lambda e: self.Option_Button_on_collision_in(Button))
        Button.bind("<Leave>",  lambda e: self.Option_Button_on_collision_out(Button))
        
    def Option_Frame_Add_Style(self,Frame) -> None:
        Frame.config(bg = self.Option_Frame["bg_color"],relief = self.Option_Frame["relief"],)

    def Option_Button_on_collision_in(self, Button):
        Button.config(bg = self.Option_Button["on_collision"])
        
    def Option_Button_on_collision_out(self, Button):
        Button.config(bg = self.Option_Button["bg_color"])
    