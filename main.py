from tkinter import Tk, Label, Button, IntVar, ttk
from components.button_pannel import ButtonPanel
from components.screen import Screen
from components.logic import Logic


# Create method that handle value from buttons
def handle_click(value):
    Logic(value)


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("700x800")

        self.total = 0
        self.raw_first_number = ""
        self.raw_second_number = ""
        self.int_first_number = 0
        self.int_second_number = 0
        self.operator = ""

        self.label_total = IntVar()
        self.label_total.set(self.total)
        self.total_label = Label(master, textvariable=self.label_total)

        self.button_panel = ButtonPanel(handle_click)  # Create the button's panel
        self.screen = Screen(self.total)  # Create the screen


root = Tk()
im_beginner = Calculator(root)
root.mainloop()
