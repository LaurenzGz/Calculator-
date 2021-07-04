equation = "231 + sinln"
#x = eval(equation)


equation = equation.replace(" ", "")
print(equation)
if equation[-3:-1] == "nl":
    equation = equation[:-2]
elif equation[-1] == "n" or "s":
    equation = equation[:-1]

print(equation)

#print(x)

