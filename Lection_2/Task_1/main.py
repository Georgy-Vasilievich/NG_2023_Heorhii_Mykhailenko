list = []

number = int(input("How many elements do you want to enter? "))

for element in range(number):
	list.append(input("Element {}: ".format(element)))

search = input("Enter the element you want to search for: ")

print("Occurrences:", list.count(search))
