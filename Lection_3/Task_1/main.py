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

def inputNumber(name):
	return float(input("Enter {} number: ".format(name)))

def inputOperation():
	return input("Enter the operation: ")

def inputData():
	number1 = inputNumber("the first")
	number2 = inputNumber("the second")
	operation = inputOperation()
	return number1, number2, operation

def calculation(number1, number2, operation):
	match operation:
		case "+":
			result = addition(number1, number2)
		case "-":
			result = subtraction(number1, number2)
		case "*":
			result = multiplication(number1, number2)
		case "/":
			result = division(number1, number2)
	return result

def outputResult(result):
	print(result)

def finalAction(result):
	if result != None and result >= 0:
		print("Square root:", squareRoot(result))


result = calculation(*inputData())
outputResult(result)
finalAction(result)
