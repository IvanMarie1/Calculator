import re


def operation(a: float, b: float, operator: str) -> float:
    """Return the result of a basic operation
    
    Only [ + - * / ] supported"""
    result = 0
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        try:
            result = a / b
        except ZeroDivisionError:
            print("You can't divide by zero")
    return result

def closed_parenthesis(text, i_start) -> int:
    """Return the index at which the parenthesis is closed, if not raise an error"""
    i_end = i_start + 1

    while i_end < len(text):
        if text[i_end] == "(":
            i_end = closed_parenthesis(text, i_end)
        elif text[i_end] == ")":
            return i_end
        i_end += 1
    
    raise SyntaxError('Parenthesis not closed')

def simplify(number: str) -> int | float:
    """Convert a string number into int or float according to its value
    
    If it is not a number, return 0"""
    try:
        result = float(number)
        if result.is_integer():
            return int(result)
        return result
    except ValueError:
        print("Invalid Syntax")
        return 0

def split_calculation(calc: str) -> list[str]:
    """Split a calculation in different element : parenthesis until it's closed, numbers, operators
    
    Return a list of the calcultion's terms"""
    terms = []
    i_start = 0
    i_end = 0

    while i_end < len(calc):
        if calc[i_end] == '(':
            # append what is before the parenthesis
            terms += my_split(calc, i_start, i_end)
            # append the content of the parenthesis
            i_start = i_end
            i_end = closed_parenthesis(calc, i_end)
            terms.append(calc[i_start:i_end+1])
            i_start = i_end+1
        i_end += 1
    # append the last term
    terms += my_split(calc, i_start, i_end)
    return terms


def my_split(text, i_start, i_end):
    """Split a calculation with re module

    Return a list of the splited numbers and operators"""
    my_pattern = r'(\+|(?<![/*+])-|\/|\*)'
    my_first_pattern = r'(\+|(?<![/*+])(?!^-)-|\/|\*)'

    if i_start == 0:
        return ' '.join(re.split(my_first_pattern, text[:i_end])).split() # handle first neg number
    return ' '.join(re.split(my_pattern, text[i_start:i_end])).split()




def calculate(calc: str) -> float:
    """Return the result of a calculation string

    Only support [ + - * / ]

    ---
    TODO 
    - add other operators like exponent, sqrt, etc.
    - "intelligent" caluculations like (2+3)(2-3) without operator
    """

    # only supported characters
    supported_char = list('0123456789+-*/.()')
    for char in calc:
        if char not in supported_char:
            print("Unknown character")
            return 0
    
    # if it is englobed by parentheses, remove them
    if calc.startswith('('):
        if closed_parenthesis(calc, 0) == len(calc) - 1:
            calc = calc[1:-1]


    # splitting the calculation
    terms = split_calculation(calc)
    if len(terms) <= 1:
        return simplify(calc)

    # finding the last operation
    priority = {"*": 1, "/": 1, "+": 2, "-": 2}
    max_priority = 0
    i_operator = 0
    for i in range(len(terms)):
        if terms[i] in '+-*/':
            if priority[terms[i]] >= max_priority:
                max_priority = priority[terms[i]]
                i_operator = i
    

    operator = terms[i_operator]
    left_term = calculate(''.join(terms[:i_operator]))
    right_term = calculate(''.join(terms[i_operator+1:]))
    return operation(left_term, right_term, operator)
        



if __name__ == "__main__":
    print(calculate('-5+(5+3)-5'))