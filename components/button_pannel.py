from tkinter import Tk, Label, Button, IntVar, ttk
from components.button import ButtonSingle


class ButtonPanel:

    #  Create the button's panel
    def __init__(self, handle_click):

        #  Create each buttons
        ButtonSingle("+", 5, 1, 3, handle_click)
        ButtonSingle("-", 5, 2, 3, handle_click)
        ButtonSingle("*", 5, 3, 3, handle_click)
        ButtonSingle("/", 5, 4, 3, handle_click)
        ButtonSingle("=", 5, 5, 3, handle_click)
        ButtonSingle("AC", 5, 1, 0, handle_click)
        ButtonSingle("+/-", 5, 1, 1, handle_click)
        ButtonSingle(".", 5, 5, 2, handle_click)
        ButtonSingle("%", 5, 1, 2, handle_click)
        ButtonSingle(1, 5, 4, 0, handle_click)
        ButtonSingle(2, 5, 4, 1, handle_click)
        ButtonSingle(3, 5, 4, 2, handle_click)
        ButtonSingle(4, 5, 3, 0, handle_click)
        ButtonSingle(5, 5, 3, 1, handle_click)
        ButtonSingle(6, 5, 3, 2, handle_click)
        ButtonSingle(7, 5, 2, 0, handle_click)
        ButtonSingle(8, 5, 2, 1, handle_click)
        ButtonSingle(9, 5, 2, 2, handle_click)
        ButtonSingle(0, 11, 5, 0, handle_click)

