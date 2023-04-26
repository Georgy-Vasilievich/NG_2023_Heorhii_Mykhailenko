import sys

list = []

try:
    number = int(input("How many elements do you want to enter? "))
except ValueError:
    print("A number is required.")
    sys.exit(1)

for element in range(number):
    list.append(input("Element {}: ".format(element)))

search = input("Enter the element you want to search for: ")

print("Occurrences:", list.count(search))
