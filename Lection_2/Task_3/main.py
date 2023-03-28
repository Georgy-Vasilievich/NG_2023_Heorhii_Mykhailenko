list = [[], [], []]
elements = set()

for i in range(3):
	number = int(input("How many elements do you want to enter in the list {}? ".format(i)))
	
	for j in range(number):
		list[i].append(input("Element {}: ".format(j)))

	for element in list[i]:
		if list[i].count(element) > 1:
			elements.add(element)

print("Non-unique elements:", elements)
