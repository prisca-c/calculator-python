from tkinter import Tk, Label, IntVar
from components.button_pannel import ButtonPanel
from components.screen import Screen
from components.Logic.logic import Logic


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("250x250")

        self.total = 0

        self.button_panel = ButtonPanel()  # Create the button's panel
        self.screen = Screen(self.total)  # Create the screen


root = Tk()
im_beginner = Calculator(root)
root.mainloop()
