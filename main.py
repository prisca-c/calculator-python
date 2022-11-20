from tkinter import Tk
from components.button_pannel import ButtonPanel
from components.screen import Screen
from components.Logic.logic import Logic


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("250x250")

        self.total = 0

        #  Handle the screen display whenever total changes
        def handle_screen():
            Screen(Logic.screen)

        handle_screen()
        self.button_panel = ButtonPanel(handle_screen)  # Create the button's panel


root = Tk()
im_beginner = Calculator(root)
root.mainloop()
