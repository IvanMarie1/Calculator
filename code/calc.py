import re


def operation(a: float, b: float, operator: str) -> float | str:
    """Return the result of a basic operation
    
    Only [ + - * / ] supported
    
    Return "ZeroDivisionError" if you divide by zero"""
    
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
            return "Zero Division Error"
    return result


def closed_parenthesis(text, i_start) -> int:
    """Return the index at which the parenthesis is closed, if not return a text error"""
    i_end = i_start + 1

    while i_end < len(text):
        if text[i_end] == "(":
            i_end = closed_parenthesis(text, i_end)
        elif text[i_end] == ")":
            return i_end
        i_end += 1
    return "\"(\" not closed"


def simplify(number: str) -> int | float | str:
    """Convert a string number into int or float according to its value
    
    If it is not a number, return a text error"""
    try:
        result = float(number)
        if result.is_integer():
            return int(result)
        return result
    except ValueError:
        return "Invalid Syntax"

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
            if isinstance(i_end, str):
                return i_end
            terms.append(calc[i_start:i_end+1])
            i_start = i_end+1
        i_end += 1
    # append the last term
    terms += my_split(calc, i_start, i_end)
    return terms


def my_split(text, i_start, i_end) -> list[str]:
    """Split a calculation with re module

    Return a list of the splited numbers and operators"""
    my_pattern = r'(\+|(?<![/*+])-|\/|\*)'
    my_first_pattern = r'(\+|(?<![/*+])(?!^-)-|\/|\*)'

    if i_start == 0:
        return ' '.join(re.split(my_first_pattern, text[:i_end])).split() # handle first neg number
    return ' '.join(re.split(my_pattern, text[i_start:i_end])).split()




def calculate(calc: str) -> float | str:
    """Return the result of a calculation string

    Only support [ + - * / ]

    If an error occurs, it returns an error message

    ---
    TODO 
    - add other operators like exponent, sqrt, etc.
    - "intelligent" caluculations like (2+3)(2-3) without operator
    """

    # only supported characters
    supported_char = list('0123456789+-*/.()')
    for char in calc:
        if char not in supported_char:
            return "Unknown character"
    
    # if it is englobed by parentheses, remove them
    if calc.startswith('('):
        if closed_parenthesis(calc, 0) == len(calc) - 1:
            calc = calc[1:-1]


    # splitting the calculation
    terms = split_calculation(calc)
    if isinstance(terms, str): # not closed parenthesis
        return terms
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
    if isinstance(left_term, str):
        return left_term
    elif isinstance(right_term, str):
        return right_term
    return operation(left_term, right_term, operator)
