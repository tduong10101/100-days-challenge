from art import logo
import os
#add
def add(n1, n2):
    return n1 + n2
#substract
def substract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
def calculator():
    clear()
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    continue_cal = "y"
    while continue_cal == "y":
        operations_symbol = ""
        while operations_symbol not in operations:
            operations_symbol = input("Pick an operaation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        continue_cal = ""
        while not (continue_cal == "y" or continue_cal == "n" or continue_cal == "e"):
            continue_cal = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculator, or 'e' exit: ")
    if continue_cal == 'n':
        calculator()

calculator()