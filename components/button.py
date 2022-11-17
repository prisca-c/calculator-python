from tkinter import Button


class ButtonSingle:

    #  Create a reusable button
    def __init__(self, value, row, column, handle_click):
        btn = Button(text=value, command=lambda: handle_click(value))
        if value == "=" or value == "/" or value == "*" or value == "-" or value == "+":
            btn.configure(bg="orange")

        if value == "0":
            btn.configure(width=13, height=2)
            btn.grid(row=row, column=column, columnspan=2)
        else:
            btn.configure(width=6, height=2)
            btn.grid(row=row, column=column)

