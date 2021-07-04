import math

x = "sin(720)"
i = x.index("sin(")


def replace_trigo() -> None:
    """This function is used to replace all trigo function in the equation to their answer"""
    find_sin()
    find_cos()
    find_tan()

def find_sin() -> None:
    global x
    while "sin" in x:
        x = symbols('x')
        f = cos(x)
        print(N(f.subs(x, math.radians(2880))))
        i = x.index("sin")
        num = find_number_trigo(i)
        ans = round(math.sin(Decimal(num)*Decimal(math.pi/ 180)),10)
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
        ans = math.sin(float(num)*(math.pi/ 180))
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
        ans = math.sin(float(num)*(math.pi/ 180))
        replace_word = f"tan({num})"
        x = x.replace(replace_word, str(ans))
        replace_word = f"tan{num}"
        x = x.replace(replace_word, str(ans))
        print(x)

def find_number_trigo(i: int) -> str:
    """to extract the number from a trigo expression;i is the index of the expression"""
    global x
    loop = True
    while loop:
        n = ""
        #print(x[i])
        try:
            data = float(x[i])
        except:
            data = "str"
        if data != "str":
            while True:
                try:
                    data = float(x[i])
                except:
                    if i > len(x) - 1:
                        break
                    if x[i] == ".":
                        data = "float"
                        n += x[i]
                        i += 1
                    else:
                        loop = False
                        break
                n += x[i]
                i += 1
        i+=1
        if i > len(x) - 1:
            break
    return n



#replace_trigo()


print(math.degrees(math.asin(14)))


#print(eval("sin(90)"))