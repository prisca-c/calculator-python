from tkinter import Tk, Label, Button, IntVar, ttk
from components.button import ButtonSingle
from components.Logic.logic import Logic


class ButtonPanel:

    #  Create the button's panel
    def __init__(self):

        def handle_click(btn_value):
            Logic(btn_value)

        #  Create each buttons
        ButtonSingle("+", 1, 3, handle_click)
        ButtonSingle("-", 2, 3, handle_click)
        ButtonSingle("*", 3, 3, handle_click)
        ButtonSingle("/", 4, 3, handle_click)
        ButtonSingle("=", 5, 3, handle_click)
        ButtonSingle("AC", 1, 0, handle_click)
        ButtonSingle("+/-", 1, 1, handle_click)
        ButtonSingle(".", 5, 2, handle_click)
        ButtonSingle("%", 1, 2, handle_click)
        ButtonSingle("1", 4, 0, handle_click)
        ButtonSingle("2", 4, 1, handle_click)
        ButtonSingle("3", 4, 2, handle_click)
        ButtonSingle("4", 3, 0, handle_click)
        ButtonSingle("5", 3, 1, handle_click)
        ButtonSingle("6", 3, 2, handle_click)
        ButtonSingle("7", 2, 0, handle_click)
        ButtonSingle("8", 2, 1, handle_click)
        ButtonSingle("9", 2, 2, handle_click)
        ButtonSingle("0",  5, 0, handle_click)

