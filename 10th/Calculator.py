from art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div

}
def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Enter the first number: "))
    while should_continue:
        for op in operations:
            print(op)
        operation_symbol = input("Select from from the following: ")
        num2 = int(input("Enter the next number: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        restart = input(f"Enter 'y' continue with {answer} or 'n' To Restart the program: ")

        if restart == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" *20)
            calculator()

calculator()





