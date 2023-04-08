import math

def addition(firstSummand, secondSummand):
	return firstSummand + secondSummand

def subtraction(minuend, subtrahend):
	return minuend - subtrahend

def multiplication(firstFactor, secondFactor):
	return firstFactor * secondFactor

def division(dividend, divisor):
	if divisor != 0:
		return dividend / divisor

def squareRoot(radicand):
	if radicand >= 0:
		return math.sqrt(radicand)

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation: ")
result = None

match operation:
	case "+":
		result = addition(number1, number2)
	case "-":
		result = subtraction(number1, number2)
	case "*":
		result = multiplication(number1, number2)
	case "/":
		result = division(number1, number2)

if result != None:
	print(result)
	print("Square root:", squareRoot(result))
