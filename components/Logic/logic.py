from components.Logic.operators import Operators


class Logic:

    def __init__(self, value):

        self.value = value

        print(self.value)

        if self.value == "=" or self.value == "/" or self.value == "*" or self.value == "-" or self.value == "+":
            Operators(self.value)

        def clear():
            print("clear")

        def change_sign():
            print("change_sign")

        def add_decimal():
            print("add_decimal")

        def percent():
            print("percent")

        if self.value == "AC":
            clear()

        if self.value == "+/-":
            change_sign()

        if self.value == ".":
            add_decimal()

        if self.value == "%":
            percent()

        #  Operators(self.value)
