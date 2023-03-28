list = []

number = int(input("How many elements do you want to enter? "))

for i in range(number):
	list.append(input("Element {}: ".format(i)))

unique = set(list)

print("Unique elements:", unique)
