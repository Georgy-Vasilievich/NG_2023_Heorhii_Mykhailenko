list = []

occurrences = 0

number = int(input("How many elements do you want to enter? "))

for element in range(number):
	list.append(input("Element {}: ".format(element)))

search = input("Enter the element you want to search for: ")

for element in range(number):
	if list[element] == search:
		occurrences += 1

print("Occurrences:", occurrences)
