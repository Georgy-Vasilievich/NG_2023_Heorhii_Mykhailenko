def askTitle():
	return input("Enter the title: ")

def askAuthor():
	return input("Enter the author: ")

def askYear():
	return int(input("Enter the publication year: "))

def askPages():
	return int(input("Enter the number of pages: "))

def askGenre():
	return input("Enter the genre: ")

def askBinding():
	return input("Enter the binding: ")

def addBook(bookList):
	title = askTitle()
	author = askAuthor()
	year = askYear()
	pages = askPages()
	genre =  askGenre()
	binding = askBinding()
	bookList.append({"title": title, "author": author, "year": year, "pages": pages, "genre": genre, "binding": binding})

def deleteBook(bookList):
	title = askTitle()
	for book in bookList:
		if book["title"] == title:
			bookList.remove(book)
			print("Deleted.")

def editBook(bookList):
	title = askTitle()
	for book in bookList:
		if book["title"] == title:
			edit = input('''1 - Title
2 - Author
3 - Publication year
4 - Number of pages
5 - Genre
6 - Binding

Enter a number: ''')

			match int(edit):
				case 1:
					book["title"] = askTitle()
				case 2:
					book["author"] = askAuthor()
				case 3:
					book["year"] = askYear()
				case 4:
					book["pages"] = askPages()
				case 5:
					book["genre"] = askGenre()
				case 6:
					book["binding"] = askBinding()
				case _:
					print("Invalid input.")

def searchBook(bookList):
	type = input('''Search by:
1 - Title
2 - Author
3 - Publication year
4 - Genre

Enter a number: ''')

	match int(type):
		case 1:
			title = askTitle()
			for book in bookList:
				if book["title"] == title:
					print(book)
		case 2:
			author = askAuthor()
			for book in bookList:
				if book["author"] == author:
					print(book)
		case 3:
			year = askYear()
			for book in bookList:
				if book["year"] == year:
					print(book)
		case 4:
			genre = askGenre()
			for book in bookList:
				if book["genre"] == genre:
					print(book)
		case _:
			print("Invalid input.")


books = [{"title": "Harry Potter and the Philosopher's Stone", "author": "JK Rowling", "year": 1997, "pages": 223, "genre": "Fantasy", "binding": "Hardback"},
	{"title": "The Hunger Games", "author": "Suzanne Collins", "year": 2008, "pages": 374, "genre": "Fiction", "binding": "Paperback"},
	{"title": "The Catcher in the Rye", "author": "JD Salinger", "year": 1951, "pages": 234, "genre": "Fiction", "binding": "Paperback"}]

while True:
	choice = input('''1 - Add a book
2 - Delete a book
3 - Edit a book
4 - Search a book

Enter a number: ''')

	match int(choice):
		case 1:
			addBook(books)
		case 2:
			deleteBook(books)
		case 3:
			editBook(books)
		case 4:
			searchBook(books)
		case _:
			print("Invalid input.")
