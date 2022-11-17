from tkinter import Tk, Label, IntVar


class Screen:

    def __init__(self, master, total_value):
        self.master = master
        self.label_total = IntVar()
        self.label_total.set(total_value)
        self.total_label = Label(master, textvariable=self.label_total)
        self.total_label.grid(row=0, column=0, columnspan=4)
        self.total_label.configure(width=25, height=2, bg="grey", fg="white")