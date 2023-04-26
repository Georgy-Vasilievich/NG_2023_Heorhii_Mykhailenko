import sys

size = 3

sets = []

setsCombined = []

elements = set()

for setNumber in range(size):
    sets.append(set())
    try:
        number = int(input("How many elements do you want to enter in the set {}? ".format(setNumber)))
    except ValueError:
        sys.exit("A number is required.")

    for element in range(number):
        value = input("Element {}: ".format(element))
        sets[setNumber].add(value)
        
    setsCombined += list(sets[setNumber])
    
    
for element in setsCombined:
    if setsCombined.count(element) > 1:
        elements.add(element)

print("Non-unique elements:", elements)
