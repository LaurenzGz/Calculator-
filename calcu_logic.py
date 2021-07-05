import math


#----Global variables here-----
equation = ""  # variable that stores all the inputs
syntax_flag, syntax_logarithm, syntax_trigonometry,syntax_inversetrigonometry = 0,0,0,0  #variable that acts as a flag if there is syntax error

symbols = ["++", "--", "**", "//", "÷÷"]
trigonometry = ["sin", "cos", "tan","arcsin", "arccos", "arctan"]
logarithms = ["ln", "e", "log"]
squar_root = "√"
answer_button = "0" #default answer value to zero
chain = False #This flag will deside if the calculation will automatically chain (input ANS by default)
deg_rad = True #the calculator is in degrees mode if True, and rad mode if false, it is degrees mode in default.

#----------calculator functions-----------
def calculate() -> str:
    """this executes the equation"""
    global equation, syntax_flag, syntax_logarithm, syntax_trigonometry,syntax_inversetrigonometry
    global answer_button, chain
    find_ans()

    #check for double symbol errors
    for s in symbols:
        if s in equation:
            return "Syntax error"
    convert_symbols()
    #check for sqrt
    if squar_root in equation:
        examine_sqrt()
    #check if there is trigonometry in the equation
    for t in trigonometry:
        if t in equation:
            examine_trigo() #convert all trigo to numerical
            break
    #check if there is logarithms in equation
    for l in logarithms:
        if l in equation:
            examine_logarithm()
            break

    if syntax_inversetrigonometry:
        return "math domain error"   # when inverse trigo is given out of range
    elif syntax_trigonometry:
        return "Syntax error"
    elif not equation:
        return "0"     #when input is empty, it equals to zero
    try:
        syntax_flag, syntax_logarithm, syntax_trigonometry,syntax_inversetrigonometry = 0,0,0,0
        answer_button = str(eval(equation))
        equation = ""
        chain = True
        return answer_button
    except ZeroDivisionError:
        return "Math zero divison error"
    except:
        return "Syntax error"

def clear_all() -> None:
    """This function will make the equation an empty string"""
    global equation, syntax_flag, chain
    equation = ""
    syntax_flag,syntax_logarithm, syntax_trigonometry = 0,0,0
    chain = False

def delete() -> None:
    """This function will delete certain characters from the equation"""
    global equation
    equation = equation.replace(" ", "")
    sym = "nsg"

    if equation[-3:-1] == "nl": #delete the whole "ln"
        equation = equation[:-2]
    elif equation[-1] in sym: #delete the whole sin, cos, tan, log
        equation = equation[:-3]
    elif equation:
        equation = equation[:-1] #delete one character symbols and number


def ans() -> None:
    """This function will input ans ---
    the calculator will automatical save the last calculation in to the variable "ans" """
    global equation, chain
    equation += "ans"
    chain = False



#----------------------------functions for symbols here--------------------
def addition() -> None:
    """This will add a plus symbol"""
    global equation, chain
    if chain:
        equation += "ans+"
        chain = False
    else:
        equation += "+"

def subtraction() -> None:
    """This will add a plus symbol"""
    global equation, chain
    if chain:
        equation += "ans-"
        chain = False
    else:
        equation += "-"

def division() -> None:
    """This will add a plus symbol"""
    global equation, chain
    if chain:
        equation+= "ans÷"
        chain = False
    else:
        equation += "÷"

def multiplication() -> None:
    """This will add a plus symbol"""
    global equation, chain
    if chain:
        chain = False
        equation += "ans×"
    else:
        equation += "×"

def exponent() -> None:
    """This will add a plus symbol"""
    global equation,chain
    if chain:
        equation += "ans^"
        chain=False
    else:
        equation += "^"

def negative_sign() -> None:
    """This will add a plus symbol"""
    global equation, chain
    if chain:
        equation += "﹣ans" #small hyphen-minus (﹣)
    else:
        equation += "﹣"

def parenthesis_open() -> None:
    """This will add a plus symbol"""
    global equation,chain
    equation += "("
    chain = False

def parenthesis_close() -> None:
    """This will add a plus symbol"""
    global equation, chain
    equation += ")"
    chain = False

def decimal() -> None:
    """This will add a decimal symbol"""
    global equation,chain
    equation += "."
    chain = False

def e() -> None:
    """This function will input e"""
    global equation, chain
    equation += "e"
    chain = False

def sin() -> None:
    """This will input sin"""
    global equation, chain
    if chain:
        equation += "sin(ans)"
        chain = False
    else:
        equation += "sin"

def cos() -> None:
    """This will input cos"""
    global equation, chain
    if chain:
        equation += "cos(ans)"
        chain = False
    else:
        equation += "cos"

def tan() -> None:
    """This will input tan"""
    global equation,chain
    if chain:
        equation += "tan(ans)"
        chain = False
    else:
        equation += "tan"

def arcsin() -> None:
    """This will input sin"""
    global equation, chain
    if chain:
        equation += "arcsin(ans)"
        chain = False
    else:
        equation += "arcsin"

def arccos() -> None:
    """This will input cos"""
    global equation, chain
    if chain:
        equation += "arccos(ans)"
        chain = False
    else:
        equation += "arccos"

def arctan() -> None:
    """This will input tan"""
    global equation, chain
    if chain:
        equation += "arctan(ans)"
        chain = False
    else:
        equation += "arctan"

def ln() -> None:
    """This will input ln"""
    global equation, chain
    if chain:
        equation += "ln(ans)"
        chain = False
    else:
        equation += "ln"

def log() -> None :
    """This will input log"""
    global equation, chain
    if chain:
        equation += "log(ans)"
        chain = False
    else:
        equation += "log"

def sqrt() -> None:
    """This will input √ square root"""
    global equation, chain
    if chain:
        equation += "√(ans)"
        chain = False
    else:
        equation += "√"
#---------------------------------TRIGONOMETRY FUNCTIONS-------------------------------

def examine_trigo() -> None:
    """This function is used to replace all trigo function in the equation to their answer"""
    find_asin()
    find_acos()
    find_atan()
    find_sin()
    find_cos()
    find_tan()

def find_sin() -> None:
    """This converts the sin in the equation to numerical value"""
    global equation, syntax_trigonometry
    while "sin" in equation:

        i = equation.index("sin")
        num = find_number_trigo(i)
        if num:
            if deg_rad:
                ans = round(math.sin(math.radians(float(num))),10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thesin({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thesin{num}"
                equation = equation.replace(replace_word, str(ans))
            else:
                ans = round(math.sin((float(num))), 10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thesin({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thesin{num}"
                equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "sin"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1

def find_cos() -> None:
    """This converts the cos in the equation to numerical value"""
    global equation, syntax_trigonometry
    while "cos" in equation:

        i = equation.index("cos")
        num = find_number_trigo(i)
        if num:
            if deg_rad:
                ans = round(math.cos(math.radians(float(num))), 10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thecos({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thecos{num}"
                equation = equation.replace(replace_word, str(ans))
            else:
                ans = round(math.cos((float(num))), 10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thecos({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thecos{num}"
                equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "cos"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1

def find_tan() -> None:
    """This converts the tan in the quation to numerical value"""
    global equation, syntax_trigonometry
    while "tan" in equation:

        i = equation.index("tan")
        num = find_number_trigo(i)
        if num:
            if deg_rad:
                ans = round(math.tan(math.radians(float(num))), 10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thetan({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thetan{num}"
                equation = equation.replace(replace_word, str(ans))
            else:
                ans = round(math.tan((float(num))), 10)
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thetan({num})"
                equation = equation.replace(replace_word, str(ans))
                replace_word = f"thetan{num}"
                equation = equation.replace(replace_word, str(ans))
        else:
            replace_word = "tan"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1

def find_asin() -> None:
    """This converts the arcsin in the equation to numerical value"""
    global equation, syntax_trigonometry, syntax_inversetrigonometryn
    while "arcsin" in equation:

        i = equation.index("arcsin")
        num = find_number_trigo(i)
        if num:
            try:
                ans = math.asin(float(num))
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thearcsin({num})"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
                replace_word = f"thearcsin{num}"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
            except:
                syntax_trigonometry += 1
        else:
            replace_word = "arcsin"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1
def find_acos() -> None:
    """This converts the arccos in the equation to numerical value"""
    global equation, syntax_trigonometry, syntax_inversetrigonometryn
    while "arccos" in equation:

        i = equation.index("arccos")
        num = find_number_trigo(i)
        if num:
            try:
                ans = math.acos(float(num))
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thearccos({num})"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
                replace_word = f"thearccos{num}"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
            except:
                syntax_trigonometry += 1
        else:
            replace_word = "arccos"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1
def find_atan() -> None:
    """This converts the arctan in the equation to numerical value"""
    global equation, syntax_trigonometry, syntax_inversetrigonometryn
    while "arctan" in equation:

        i = equation.index("arctan")
        num = find_number_trigo(i)
        if num:
            try:
                ans = math.atan(float(num))
                equation = equation[:i] + "the" + equation[i:]
                replace_word = f"thearctan({num})"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
                replace_word = f"thearctan{num}"
                equation = equation.replace(replace_word, str(math.degrees(ans)))
            except:
                syntax_trigonometry += 1
        else:
            replace_word = "arctan"
            equation = equation.replace(replace_word, "")
            syntax_trigonometry += 1

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
                        n += equation[i]
                        i += 1
                    elif equation[i] == "﹣":
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

#------------------------------------------------------Logarithms, e, ln-------------------------------------------------
def examine_logarithm() -> None:
    """converts any logarthm inputs into numerical value"""
    convert_e()
    find_ln()
    find_log()

def convert_e() -> None:
    """This converts the tan in the quation to numerical value"""
    global equation
    while "e" in equation:
        ans = math.e
        equation = equation.replace("e", str(ans))

def find_ln() -> None:
    """This converts the tan in the quation to numerical value"""
    global equation,syntax_inversetrigonometry
    while "ln" in equation:

        i = equation.index("ln")
        num = find_number_ln(i)
        if num:
            try:
                ans = round(math.log(float(num)), 10)
            except:
                syntax_inversetrigonometry += 1
            equation = equation[:i] + "the" + equation[i:]
            replace_word = f"theln({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"theln{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            syntax_inversetrigonometry += 1
            replace_word = "ln"
            equation = equation.replace(replace_word, "")

def find_log() -> None:
    """This converts the tan in the quation to numerical value"""
    global equation,syntax_inversetrigonometry
    while "log" in equation:

        i = equation.index("log")
        num = find_number_ln(i)
        if num:
            try:
                ans = round(math.log10(float(num)), 10)
            except:
                syntax_inversetrigonometry += 1
            equation = equation[:i] + "the" + equation[i:]
            replace_word = f"thelog({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"thelog{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            syntax_inversetrigonometry += 1
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
                        n += equation[i]
                        i += 1
                    elif equation[i] == "﹣":
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

def examine_sqrt() -> None:
    """This function converts sqrt into numerical values"""
    global equation
    while "√" in equation:

        i = equation.index("√")
        num = find_number_ln(i)
        if num:
            try:
                ans = round(math.sqrt(float(num)), 12)
            except:
                syntax_inversetrigonometry += 1
            equation = equation[:i] + "the" + equation[i:]
            replace_word = f"the√({num})"
            equation = equation.replace(replace_word, str(ans))
            replace_word = f"the√{num}"
            equation = equation.replace(replace_word, str(ans))
        else:
            syntax_inversetrigonometry += 1
            replace_word = "√"
            equation = equation.replace(replace_word, "")

#--------------------------For the exponent and negative sign symbols-------------
def convert_symbols():
    global equation
    if "^" or "﹣" or "÷" or "×" in equation:
        equation = equation.replace("^", "**")
        equation = equation.replace("﹣", "-")
        equation = equation.replace("÷", "/")
        equation = equation.replace("×", "*")

#---------------------------For the ANS button---------------------
def find_ans() -> None:
    global equation
    while "ans" in equation:
        i = equation.index("ans")
        equation = equation[:i] + "the" + equation[i:]
        equation = equation.replace("theans", answer_button)

#---------------------------------Functions for inputing numbers --------------------
def one():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "1"
    chain = False

def two():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "2"
    chain = False
def three():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "3"
    chain = False
def four():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "4"
    chain = False
def five():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "5"
    chain = False
def six():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "6"
    chain = False
def seven():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "7"
    chain = False
def eight():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "8"
    chain = False
def nine():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "9"

def zero():
    global equation,chain
    """Adding number 5 to the equation"""
    equation += "0"
    chain = False

