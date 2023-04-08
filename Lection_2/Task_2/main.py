list = []

number = int(input("How many elements do you want to enter? "))

for element in range(number):
	list.append(input("Element {}: ".format(element)))

unique = set(list)

print("Unique elements:", unique)
