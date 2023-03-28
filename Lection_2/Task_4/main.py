class BookList:
	def __init__(self, books):
		self.books = books

	def search_by_title(self, title):
		for book in self.books:
			if book.title == title:
				return book
		return False

	def search_by_author(self, author):
		books_by_author = []
		for book in self.books:
			if book.author == author:
				books_by_author.append(book)
		return books_by_author

	def search_by_publication_year(self, year):
		books_by_year = []
		for book in self.books:
			if book.year == year:
				books_by_year.append(book)
		return books_by_year

	def search_by_genre(self, genre):
		books_by_genre = []
		for book in self.books:
			if book.genre == genre:
				books_by_genre.append(book)
		return books_by_genre

	def add_book(self, book):
		self.books.append(book)

	def delete_book(self, book):
		self.books.remove(book)

	def access_book_by_number(self, number):
		return self.books[number]

	def stringify_book(self, book):
		return "{}"

class Book:
	def __init__(self, title, author, year, pages, genre, binding):
		self.title = title
		self.author = author
		self.year = year
		self.pages = pages
		self.genre = genre
		self.binding = binding

def addBook():
	title = input("Enter the title: ")
	if bookList.search_by_title(title):
		print("Such book already exists.")
		return
	bookList.add_book(Book(title, input("Enter the author: "), int(input("Enter the publication year: ")), int(input("Enter the number of pages: ")), input("Enter the genre: "), input("Enter the binding: ")))

def deleteBook():
	book = bookList.search_by_title(input("Enter the title: "))
	if book:
		bookList.delete_book(book)
	else:
		print("Not found.")

def editBook():
	book = bookList.search_by_title(input("Enter the title: "))

	if book:
		edit = input('''1 - Name
2 - Author
3 - Publication year
4 - Number of pages
5 - Genre
6 - Binding

Enter a number: ''')
	
		match int(edit):
				case 1:
					book.title = input("Enter the title: ")
				case 2:
					book.author = input("Enter the author: ")
				case 3:
					book.year = int(input("Enter the publication year: "))
				case 4:
					book.pages = int(input("Enter the number of pages: "))
				case 5:
					book.genre = input("Enter the genre: ")
				case 6:
					book.binding = input("Enter the binding: ")
				case _:
					print("Invalid input.")
	else:
		print("Not found.")

def searchBook():
	type = int(input('''1 - By title
2 - By author
3 - By year
4 - By genre

Enter a number: '''))

	list = []

	match type:
		case 1:
			book = bookList.search_by_title(input("Enter the title: "))
			if book:
				list.append(book)
			else:
				print("Not found.")
				return
		case 2:
			list = bookList.search_by_author(input("Enter the author: "))
		case 3:
			list = bookList.search_by_publication_year(int(input("Enter the publication year: ")))
		case 4:
			list = bookList.search_by_genre(input("Enter the genre: "))
		case _:
			print("Invalid input.")
			return

	if len(list) == 0:
		print("Not found.")
		return

	for book in list:
			print("{} ({}, {}) by {}, number of pages: {}, {}".format(book.title, book.year, book.genre, book.author, book.pages, book.binding))
				

books = [Book("Harry Potter and the Philosopher's Stone", "JK Rowling", 1997, 223, "Fantasy", "Hardback"),
         Book("The Hunger Games", "Suzanne Collins", 2008, 374, "Fiction", "Paperback"),
         Book("The Catcher in the Rye", "JD Salinger", 1951, 234, "Fiction", "Paperback")]

bookList = BookList(books)

while True:
	choice = input('''1 - Add a book
2 - Delete a book
3 - Edit a book
4 - Search a book

Enter a number: ''')

	match int(choice):
		case 1:
			addBook()
		case 2:
			deleteBook()
		case 3:
			editBook()
		case 4:
			searchBook()
		case _:
			print("Invalid input.")
