import re


def operation(a: float, b: float, operator: str) -> float | int | str:
    """Calculates a simple operation between two floats

    Parameters
    ---------
    a : float
        left term of the operation
    b : float
        right term of the operation
    operator : str
        symbol of the  mathematical operator (only + - * / supported)
    
    Returns
    -------
    float or int
        result of the operation (simplified)
    str
      "ZeroDivisionError" if you divide by zero"""
    
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
    return simplify(result)


def closed_parenthesis(text: str, i_start: int) -> int | str:
    """Find the index of the closing parenthesis in a string

    Parameters
    ----------
    text : str
        Text containing parentheses
    i_start : int
        Index of the opening parenthesis
    
    Returns
    -------
    int
        index at which the parenthesis is closed
    str
        "( not closed" if the parenthesis is not closed"""
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

    Parameters
    ----------
    number : str
        Number to convert type
    
    Returns
    -------
    int
        number as an integer if it is
    float
        number as a float if it is decimal
    str
        "Invalid Syntax" if it is neither
    """
    try:
        result = float(number)
        if result.is_integer():
            return int(result)
        return result
    except ValueError:
        return "Invalid Syntax"

def split_calculation(calc: str) -> list[str]:
    """Split a calculation in different element : parentheses, numbers, operators

    Parameters
    ---------
    calc : str
        Calculation line to split
    
    Returns
    -------
    list[str]
        list of the calcultion terms"""
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
    """Split numbers and operators between two indexes with re module

    Parameters
    ----------
    text : str
        Text to split up
    i_start : int
        Index of the starting position
    i_end : int
        Index of the ending position

    Returns
    -------
    list[str] 
        list of the splited numbers and operators"""
    my_pattern = r'(\+|(?<![/*+])-|\/|\*)'
    my_first_pattern = r'(\+|(?<![/*+])(?!^-)-|\/|\*)'

    if i_start == 0:
        return ' '.join(re.split(my_first_pattern, text[:i_end])).split() # first neg number included
    return ' '.join(re.split(my_pattern, text[i_start:i_end])).split()




def calculate(calc: str) -> float | int | str:
    """Give the result of a calculation line
    
    Parameters
    ----------
    calc : str
        calculation line to calculate
    
    Returns
    -------
    int | float
        result of the calculation
    str
        error message if ones occurs
    """

    # only supported characters
    supported_char = list('0123456789+-*/.()')
    for char in calc:
        if char not in supported_char:
            return "Unknown character"
    
    # if it is surronded by parentheses, remove them
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
