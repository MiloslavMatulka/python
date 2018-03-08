number1 = float(input("Insert number one: "))
number2 = float(input("Insert number two: "))
operator = input("Insert one of the operators +, -, *, /: ")

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Something went wrong.")
