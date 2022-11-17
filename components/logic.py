
def add():
    print("add")


def subtract():
    print("subtract")


def multiply():
    print("multiply")


def divide():
    print("divide")


def clear():
    print("clear")


def change_sign():
    print("change_sign")


def add_decimal():
    print("add_decimal")


def modulo():
    print("percent")


class Logic:

    def __init__(self, value):
        self.value = value

        print(self.value)

        if self.value == "+":
            add()

        if self.value == "-":
            subtract()

        if self.value == "*":
            multiply()

        if self.value == "/":
            divide()

        if self.value == "AC":
            clear()

        if self.value == "+/-":
            change_sign()

        if self.value == ".":
            add_decimal()

        if self.value == "%":
            modulo()
