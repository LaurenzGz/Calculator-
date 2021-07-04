import math


x = "sin(720) + sin(2160) + cos(2880) + 43 + 56 + tan(405)"
print(x)

def examine_trigo() -> None:
    """This function is used to replace all trigo function in the equation to their answer"""
    find_sin()
    find_cos()
    find_tan()

def find_sin() -> None:
    global x
    while "sin" in x:
        i = x.index("sin(")
        num = find_number_trigo(i)
        ans = round(math.sin(math.radians(float(num))),10)
        replace_word = f"sin({num})"
        x = x.replace(replace_word, str(ans))
        replace_word = f"sin{num}"
        x = x.replace(replace_word, str(ans))
        print(x)

def find_cos() -> None:
    global x
    while "cos" in x:
        i = x.index("cos")
        num = find_number_trigo(i)
        ans = round(math.cos(math.radians(float(num))),10)
        replace_word = f"cos({num})"
        x = x.replace(replace_word, str(ans))
        replace_word = f"cos{num}"
        x = x.replace(replace_word, str(ans))
        print(x)

def find_tan() -> None:
    global x
    while "tan" in x:
        i = x.index("tan")
        num = find_number_trigo(i)
        ans = round(math.tan(math.radians(float(num))),10)
        replace_word = f"tan({num})"
        x = x.replace(replace_word, str(ans))
        replace_word = f"tan{num}"
        x = x.replace(replace_word, str(ans))
        print(x)


def find_number_trigo(i: int) -> str:
    """to extract the number from a trigo expression;i is the index of the expression"""
    global x
    while True:
        n = ""
        if x[i] == "(":
            while True:
                i += 1
                if x[i] != ")":
                    n += x[i]
                else:
                    break
        if x[i] == ")":
            break
        i+=1
        if i > len(x) - 1:
            break
    #print(n)
    return n



examine_trigo()

  #  print(math.sin(n)))


#print(eval("sin(90)"))