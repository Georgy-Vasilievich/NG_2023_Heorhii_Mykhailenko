list = []

occurrences = 0

number = int(input("How many elements do you want to enter? "))

for i in range(number):
	list.append(input("Element {}: ".format(i)))

search = input("Enter the element you want to search for: ")

for i in range(number):
	if list[i] == search:
		occurrences += 1

print("Occurrences:", occurrences)
