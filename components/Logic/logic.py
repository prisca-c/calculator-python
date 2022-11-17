from components.Logic.operators import Operators
from components.Logic.numbers import Numbers
import re


class Logic:

    def __init__(self, value):

        self.value = value
        print(self.value + " from logic file")

        self.total = 0
        self.raw_first_number = ""
        self.raw_second_number = ""
        self.int_first_number = 0
        self.int_second_number = 0
        self.operator = ""

        #  ----------------  Operator  ---------------- #
        #  Check if the value is an operator
        #  if it is, call the operator class
        if self.value == "/" or self.value == "*" or self.value == "-" or self.value == "+":
            Operators(self.value)

        #  -----------------  Number  ----------------- #
        #  Check if value is a number with regex
        #  if it is, call the Numbers class
        if bool(re.search(r'\d', self.value)):
            Numbers(self.value)

        #  --------------  Special Character  -------------- #
        #  If value is not a number or an operator
        #  it must be a special character, and it will be handled here

        if self.value == "=":
            if self.operator == "+":
                self.total = self.int_first_number + self.int_second_number
            elif self.operator == "-":
                self.total = self.int_first_number - self.int_second_number
            elif self.operator == "*":
                self.total = self.int_first_number * self.int_second_number
            elif self.operator == "/":
                self.total = self.int_first_number / self.int_second_number

        if self.value == "AC":
            self.raw_first_number = ""
            self.raw_second_number = ""
            self.int_first_number = 0
            self.int_second_number = 0
            self.operator = ""
            self.total = 0

            print("Cleared all values")

        if self.value == "+/-":
            print("Toggle +/")

        if self.value == ".":
            print("Add decimal point")

        if self.value == "%":
            print("Add percentage")
