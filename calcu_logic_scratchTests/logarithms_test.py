import math

equation = "lne + ln8103.08392757538 + ln"
syntax_flag = 0
print((math.e)**9)

def ln_evaluate() -> None:
    convert_e()
    find_ln()

def convert_e() -> None:
    "This converts the tan in the quation to numerical value"
    global equation
    while "e" in equation:
        ans = math.e
        equation = equation.replace("e", str(ans))

def find_ln() -> None:
    "This converts the tan in the quation to numerical value"
    global equation,syntax_flag
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
            syntax_flag += 1
            replace_word = "ln"
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

#print(math.log(-1313))
print(math.log10(-123132))
