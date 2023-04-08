def drawRhombus(size, lineSize):
	asterisks = (lineSize - size) * 2 + 1
	print((size - 1) * " " + "*" * asterisks)
	if size > 1:
		drawRhombus(size-1, lineSize)
		print((size - 1) * " " + "*" * asterisks)

size = int(input("Enter the size of the half of the rhombus in lines: "))
drawRhombus(size, size)
