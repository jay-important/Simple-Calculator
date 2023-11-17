# CALCULATOR
num1 = float(input("Please input your first number"))
num2 = float(input("Please input your second number"))
symbol = input("Would you like to (A)dd, (S)ubtract, (D)ivide, or (M)ultiply")

if symbol == "+":
    total = num1 + num2
    print(num1, "+", num2, "=", total)
elif symbol == "S":
    total = num1 - num2
    print(num1, "-", num2, "=", total)
elif symbol == "D":
    total = num1 / num2
    print(num1, "+", num2, "=", total)
elif symbol == "M":
    total = num1 * num2
    print(num1,"*", num2, "=", total)
    