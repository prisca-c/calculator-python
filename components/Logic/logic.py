import re


class Logic:

    #  Define all needed variables to make the calculator work
    total = 0
    raw_first_number = ""
    raw_second_number = ""
    int_first_number = 0
    int_second_number = 0
    operator = ""

    def __init__(self, btn_value):
        self.btn_value = btn_value

        #  ----------------  Operator  ---------------- #
        #  Check if the value is an operator
        if self.btn_value == "/" or self.btn_value == "*" or self.btn_value == "-" or self.btn_value == "+":
            if Logic.operator == "":
                Logic.operator = self.btn_value
                print("Operator: " + Logic.operator)

        #  -----------------  Number  ----------------- #
        #  Check if value is a number with regex
        if bool(re.search(r'\d', self.btn_value)):
            if Logic.operator == "":
                Logic.raw_first_number += self.btn_value
                Logic.int_first_number = float(Logic.raw_first_number)
                print(Logic.raw_first_number + " raw\n" + str(Logic.int_first_number) + " int")
            else:
                Logic.raw_second_number += self.btn_value
                Logic.int_second_number = float(Logic.raw_second_number)
                print(Logic.raw_second_number + " raw\n" + str(Logic.int_second_number) + " int")

        #  --------------  Special Character  -------------- #
        #  If value is not a number or an operator
        #  it must be a special character, and it will be handled here
        if self.btn_value == "=" and Logic.raw_second_number != "":
            if Logic.operator == "+":
                Logic.total = Logic.int_first_number + Logic.int_second_number
            elif Logic.operator == "-":
                Logic.total = Logic.int_first_number - Logic.int_second_number
            elif Logic.operator == "*":
                Logic.total = Logic.int_first_number * Logic.int_second_number
            elif Logic.operator == "/":
                Logic.total = Logic.int_first_number / Logic.int_second_number
            print(Logic.total)
        #  Reset all variables
        if self.btn_value == "AC":
            Logic.raw_first_number = ""
            Logic.raw_second_number = ""
            Logic.int_first_number = 0
            Logic.int_second_number = 0
            Logic.operator = ""
            Logic.total = 0
            print("Cleared all values")
        #  Change the sign of the first number
        if self.btn_value == "+/-":
            if Logic.operator == "":
                Logic.int_first_number = Logic.int_first_number * -1
            else:
                Logic.int_second_number = Logic.int_second_number * -1
        #  Add a decimal point to the first number or the second number
        if self.btn_value == ".":
            if Logic.raw_second_number == "" and Logic.raw_first_number != "":
                Logic.raw_first_number = Logic.raw_first_number + "."
                print("First number: " + Logic.raw_first_number)
            elif Logic.raw_second_number != "":
                Logic.raw_second_number = Logic.raw_second_number + "."
                print("Second number: " + Logic.raw_second_number)
        #  Get the percentage of the first number to define the second number
        if self.btn_value == "%":
            if Logic.raw_second_number != "":
                Logic.int_second_number = Logic.int_first_number * (Logic.int_second_number / 100)
                print("Second number: " + str(Logic.int_second_number))
