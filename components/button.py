from tkinter import Button


class ButtonSingle:

    #  Create a reusable button
    def __init__(self, value, button_width, row, column, handle_click):
        btn = Button(text=value, command=lambda: handle_click(value))
        if value == "=" or value == "/" or value == "*" or value == "-" or value == "+":
            btn.configure(bg="orange")
        btn.configure(width=button_width, height=2)
        btn.columnconfigure(column, weight=1)
        if value == 0:
            btn.grid(row=row, column=column, columnspan=2)
        else:
            btn.grid(row=row, column=column)

