lists = [[], [], []]
elements = set()

for list in range(3):
	number = int(input("How many elements do you want to enter in the list {}? ".format(list)))
	
	for element in range(number):
		lists[list].append(input("Element {}: ".format(element)))

	for element in lists[list]:
		if lists[list].count(element) > 1:
			elements.add(element)

print("Non-unique elements:", elements)
