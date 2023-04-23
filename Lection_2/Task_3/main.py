size = 3

elements = set()

for listNumber in range(size):
    list = []

    number = int(input("How many elements do you want to enter in the list {}? ".format(listNumber)))

    for element in range(number):
        value = input("Element {}: ".format(element))
        list.append(value)
        if list.count(value) > 1:
            elements.add(value)

print("Non-unique elements:", elements)
