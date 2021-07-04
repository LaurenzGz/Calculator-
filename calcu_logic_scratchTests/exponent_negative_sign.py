equation = "^ ^ ^ ﹣ ﹣ ﹣"

def exponent_negativesign_convert():
    global equation
    if "^" or "﹣" in equation:
        equation = equation.replace("^", "**")
        equation = equation.replace("﹣", "-")

exponent_negativesign_convert()
print(equation)