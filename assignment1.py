import re
'''
creates a program that takes two numbers
then return there calculation based on user input
'''

def calculate(num1, num2, operation):
    """
    Purpose: one
    """
    if operation not in ['+', '-', '*', '/']:
        raise TypeError('you must use the symbols "+, -, * or /"!')
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
    except ZeroDivisionError:
        raise "you can't divide by zero"
    # end try
# end def
if __name__ == '__main__':
    users_inputs = input('enter the operation (e.g. 5 + 3):').strip()

    match = re.match(r'^(\d+(?:\.\d+)?)([+\-*/])(\d+(?:\.\d+)?)$', users_inputs.replace(' ', ''))

    if not match:
        raise ValueError("Invalid format. Please use: number operator number (e.g. 5+3 or 5 + 3)")

    num1, operation, num2 = match.groups()


    num1 = int(num1)
    num2 = int(num2)


    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

