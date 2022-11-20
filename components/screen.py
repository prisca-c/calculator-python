from tkinter import Tk, Label, IntVar


class Screen:

    def __init__(self, total_value):
        self.label_total = IntVar()
        self.label_total.set(total_value)
        self.total_label = Label(textvariable=self.label_total, anchor="e", padx=10, pady=5)
        self.total_label.grid(row=0, column=0, columnspan=4)
        self.total_label.configure(width=26, height=2, bg="grey", fg="white")

