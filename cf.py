import math
import numbers as n
import calculator_vers1 as cv

#----Global variables here-----
equation = ""  # variable that stores all the inputs
syntax_flag = 0  #variable that acts as a flag if there is syntax error
symbols = ["+", "-", "*", "/" , "**"]


#----------calculator functions-----------
def calculate() -> str:
    """this executes the equation"""
    global equation, syntax_flag
    syntax_flag = 0
    if not equation:
        return "0"     #when input is empty, it equals to zero
    try:
        if syntax_flag:
            return "Syntax error"
        else:
            return str(eval(equation))
    except:
        return "Syntax error"

def clear_all() -> None:
    global equation, syntax_flag
    equation = ""
    syntax_flag = 0

#----------------------------functions for symbols here--------------------
def addition() -> None:
    """This will add a plus symbol"""
    global equation
    global syntax_flag
    if equation:
        if equation[-1] in symbols:
            syntax_flag += 1
            equation += "+"
        else:
            equation += "+"
    else:
        equation += "+"

def subtraction() -> None:
    """This will add a plus symbol"""
    global equation
    global syntax_flag
    if equation:
        if equation[-1] in symbols:
            syntax_flag += 1
            equation += "-"
        else:
            equation += "-"
    else:
        equation += "-"

def division() -> None:
    """This will add a plus symbol"""
    global equation
    global syntax_flag
    if equation:
        if equation[-1] in symbols:
            syntax_flag += 1
            equation += "/"
        else:
            equation += "/"
    else:
        equation += "/"

def multiplication() -> None:
    """This will add a plus symbol"""
    global equation
    global syntax_flag
    if equation:
        if equation[-1] in symbols:
            syntax_flag += 1
            equation += "*"
        else:
            equation += "*"
    else:
        equation += "*"

def exponent() -> None:
    """This will add a plus symbol"""
    global equation
    global syntax_flag
    if equation:
        if equation[-1] in symbols:
            syntax_flag += 1
            equation += "**"
        else:
            equation += "**"
    else:
        equation += "**"

def negative_sign() -> None:
    """This will add a plus symbol"""
    global equation
    equation += "-"

def parenthesis_open() -> None:
    """This will add a plus symbol"""
    global equation
    equation += "("

def parenthesis_close() -> None:
    """This will add a plus symbol"""
    global equation
    equation += ")"

def decimal() -> None:
    """This will add a decimal symbol"""
    global equation
    equation += "."

#---------------------------------Functions for inputing numbers --------------------
def one():
    global equation
    """Adding number 5 to the equation"""
    equation += "1"
def two():
    global equation
    """Adding number 5 to the equation"""
    equation += "2"
def three():
    global equation
    """Adding number 5 to the equation"""
    equation += "3"
def four():
    global equation
    """Adding number 5 to the equation"""
    equation += "4"

def five():
    global equation
    """Adding number 5 to the equation"""
    equation += "5"
def six():
    global equation
    """Adding number 5 to the equation"""
    equation += "6"
def seven():
    global equation
    """Adding number 5 to the equation"""
    equation += "7"
def eight():
    global equation
    """Adding number 5 to the equation"""
    equation += "8"
def nine():
    global equation
    """Adding number 5 to the equation"""
    equation += "9"
def zero():
    global equation
    """Adding number 5 to the equation"""
    equation += "0"




print(calculate())
