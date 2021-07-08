import math


#----Global variables here-----
equation = ""  # variable that stores all the inputs
syntax_flag, syntax_logarithm, syntax_trigonometry = 0,0,0  #variable that acts as a flag if there is syntax error
trigo_flag, ln_flag,log_flag, = 0,0,0                       #variable to check if trigo,ln,log equation is used
symbols = ["+", "-", "*", "/", "**"]
answer_button = ""

#----------calculator functions-----------
def calculate() -> str:
    """this executes the equation"""
    global equation, syntax_flag, syntax_logrithm, syntax_trigonometry, answer_button
    #print(equation)
    if trigo_flag:
        examine_trigo()    # to convert any trigonometry from the equation to their numerical value
    if ln_flag:
        examine_ln()
    if not equation:
        return "0"     #when input is empty, it equals to zero
    try:
        if syntax_flag:
            syntax_flag = 0
            return "Syntax error"
        else:
            syntax_flag = 0
            answer_button = str(eval(equation))
            return answer_button
    except:
        return "Syntax error"

def clear_all() -> None:
    """This function will make the equation an empty string"""
    global equation, syntax_flag
    equation = ""
    syntax_flag,syntax_logarithm, syntax_trigonometry = 0,0,0

def delete() -> None:
    """This function will delete certain characters from the equation"""
    global equation, syntax_flag, trigo_flag
    equation = equation.replace(" ", "")
    sym = "nsg"

    if equation[-3:-1] == "nl": #delete the whole "ln"
        equation = equation[:-2]
    elif equation[-1] in sym: #delete the whole sin, cos, tan, log
        equation = equation[:-3]
    else:
        equation = equation[:-1] #delete one character symbols and number

    equation = ""
    syntax_flag = 0

#----------------------------functions for symbols here--------------------
def addition() -> None:
    """This will add a plus symbol"""
    global equation
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

def e() -> None:
    """This function will input e"""
    global equation, ln_flag
    ln_flag += 1
    equation += "e"

def sin() -> None:
    """This will input sin"""
    global equation, trigo_flag
    trigo_flag += 1
    equation += "sin"

def cos() -> None:
    """This will input cos"""
    global equation, trigo_flag
    trigo_flag += 1
    equation += "cos"

def tan() -> None:
    """This will input tan"""
    global equation, trigo_flag
    trigo_flag += 1
    equation += "tan"

def ln() -> None:
    """This will input ln"""
    global equation
    equation += "ln"

def log() -> None :
    """This will input log"""
    global equation
    equation += "log"
#---------------------------------TRIGONOMETRY FUNCTIONS-------------------------------

def examine_trigo() -> None:
    """This function is used to replace all trigo function in the equation to their answer"""
    find_sin()
    find_cos()
    find_tan()

def find_sin() -> None:
    """This converts the sin in the equation to numerical value"""
    global equation
    while "sin" in equation:

        i = equation.index("sin")
        num = find_number_trigo(i)
        if num:
            ans = round(math.sin(math.radians(float(num))),10)
            replace_word = f"sin({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"sin{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "sin"
            equation = equation.replace(replace_word, "")

def find_cos() -> None:
    "This converts the cos in the equation to numerical value"
    global equation
    while "cos" in equation:

        i = equation.index("cos")
        num = find_number_trigo(i)
        if num:
            ans = round(math.cos(math.radians(float(num))), 10)
            replace_word = f"cos({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"cos{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "cos"
            equation = equation.replace(replace_word, "")


def find_tan() -> None:
    "This converts the tan in the quation to numerical value"
    global equation
    while "tan" in equation:

        i = equation.index("tan")
        num = find_number_trigo(i)
        if num:
            ans = round(math.tan(math.radians(float(num))), 10)
            replace_word = f"tan({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"tan{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "tan"
            equation = equation.replace(replace_word, "")

def find_number_trigo(i: int) -> str:
    """to extract the number from a trigo expression;i is the index of the expression"""
    global equation
    loop = True
    while loop:
        n = ""
        try:
            data = float(equation[i])
        except:
            data = "str"
        if data != "str":
            while True:
                try:
                    data = float(equation[i])
                except:
                    if i > len(equation) - 1:
                        break
                    if equation[i] == ".":
                        data = "float"
                        n += equation[i]
                        i += 1
                    else:
                        loop = False
                        break
                n += equation[i]
                i += 1
        i += 1
        if i > len(equation) - 1:
            break
    return n

#--------------------------------Logarithms, e, ln--------------------
def examine_ln() -> None:
    convert_e()
    find_ln()
    find_log()

def convert_e() -> None:
    "This converts the tan in the quation to numerical value"
    global equation
    while "e" in equation:
        ans = math.e
        equation = equation.replace("e", str(ans))

def find_ln() -> None:
    "This converts the tan in the quation to numerical value"
    global equation,syntax_logarithm
    while "ln" in equation:

        i = equation.index("ln")
        num = find_number_ln(i)
        if num:
            ans = round(math.log(float(num)), 10)
            replace_word = f"ln({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"ln{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            syntax_logarithm += 1
            replace_word = "ln"
            equation = equation.replace(replace_word, "")

def find_log() -> None:
    "This converts the tan in the quation to numerical value"
    global equation,syntax_logarithm
    while "log" in equation:

        i = equation.index("log")
        num = find_number_ln(i)
        if num:
            ans = round(math.log10(float(num)), 10)
            replace_word = f"log({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"log{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            syntax_logarithm += 1
            replace_word = "log"
            equation = equation.replace(replace_word, "")

def find_number_ln(i: int) -> str:
    """to extract the number from an ln expression
    i is the index of the expression"""
    global equation
    loop = True
    while loop:
        n = ""
        try:
            data = float(equation[i])
        except:
            data = "str"
        if data != "str":
            while True:
                try:
                    data = float(equation[i])
                except:
                    if i > len(equation) - 1:
                        break
                    if equation[i] == ".":
                        data = "float"
                        n += equation[i]
                        i += 1
                    else:
                        loop = False
                        break
                n += equation[i]
                i += 1
        i += 1
        if i > len(equation) - 1:
            break
    return n

#---------------------------For the ANS button---------------------
def find_ans() -> None:
    global equation
    while "ans" in equation:
        i = equation.index("ans")
        equation = equation[:i] + "the" + equation[i:]
        equation = equation.replace("theans", answer_button)
        print(equation)

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

equation = "1 + 1"
print(calculate())
equation = "ans + 3"
find_ans()