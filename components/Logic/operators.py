
class Operators:

    def __init__(self, value):
        self.value = value

        def add():
            print("add")

        def subtract():
            print("subtract")

        def multiply():
            print("multiply")

        def divide():
            print("divide")

        if self.value == "+":
            add()

        if self.value == "-":
            subtract()

        if self.value == "*":
            multiply()

        if self.value == "/":
            divide()
