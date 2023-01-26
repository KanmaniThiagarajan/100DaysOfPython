from replit import clear  #clear() function
from art import logo #print ascii art from art module

# below are the functions for the four mathematical operation which is used to build calculator

# addition function
def add(n1, n2):
    return n1 + n2


# subtraction function
def sub(n1, n2):
    return n1 - n2


# multiply function
def multi(n1, n2):
    return n1 * n2


# division function
def divide(n1, n2):
    return n1 / n2


def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))  # input of first number to start the operation
    operations = {"+": add, "-": sub, "*": multi,
                  "/": divide}  # creating dictionary to store operation symbol and its function
    for symbols in operations:
        print(symbols)  # printing out all the symbols(keys from dictionary) for user to pickup an operation

    should_end = False  # setting flag as false to start with as the while loop has to continue until its true
    while not should_end:
        symbol = input("Pick out an operation: ")  # operation symbol to be given as input by user
        num2 = float(input("Enter next number: "))  # second number
        calculation = operations[symbol]  # eg calculation=operation[+]
        # calculation=add
        answer = calculation(num1, num2)  # answer=add(num1,num2) --> this calls the addition function
        print(f"{num1} {symbol} {num2} = {answer}")
        to_continue = input(
            f"Type y to continue with the {answer}, n to start an new operation: ")  # if the user wants to continue the
        # operation with the previous answer, then the answer becomes the num1, hence the function starts again by
        # asking operation symbol and next number
        if to_continue == 'y':
            num1 = answer
            # to avoid the whole below part is why we are looping in while condition is true for asking the next op
            # and number
            # num3 = float(input("Enter next number: ")) for symbols in operations: print(symbols)
            # next_symbol=input("Pick an operation: ") next_calculation=operations[next_symbol] next_answer =
            # next_calculation(answer, num3) print(f"{answer} {next_symbol} {num3} = {next_answer}") everything from
            # line 32 to 39 repeats:
        elif to_continue == "n":  # if user wants t start new operation flag is set to true , to exit from this while
            # loop start from beginning... recursive function starts here as we are calling the calculator() function
            # to start everything from beginning this build has no end as we are calling it in recursive, a function
            # calls itself inside the function
            print("starting new operation")
            should_end = True
            clear() #before starting new operation from beginning clear the previous screen
            calculator()
            # everything from line 23 repeats


calculator()
