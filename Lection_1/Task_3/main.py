import math

number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))
operation = input ("enter the operation: ")
result = None

match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2==0:
            print("division by zero")
        else:
            result = number1 / number2

if result != None:
    print(result)
    print("Square root:", math.sqrt(result))
