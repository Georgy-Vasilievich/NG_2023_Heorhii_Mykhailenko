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
			title = input("Enter the title: ")
			author = input("Enter the author: ")
			year = int(input("Enter the publication year: "))
			pages = int(input("Enter the number of pages: "))
			genre =  input("Enter the genre: ")
			binding = input("Enter the binding: ")
			books.append({"title": title, "author": author, "year": year, "pages": pages, "genre": genre, "binding": binding})

		case 2:
			title = input("Enter the title: ")
			for book in books:
				if book["title"] == title:
					books.remove(book)
					print("Deleted.")
		case 3:
			title = input("Enter the title: ")
			for book in books:
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
							book["title"] = input("Enter the title: ")
						case 2:
							book["author"] = input("Enter the author: ")
						case 3:
							book["year"] = int(input("Enter the publication year: "))
						case 4:
							book["pages"] = int(input("Enter the number of pages: "))
						case 5:
							book["genre"] = input("Enter the genre: ")
						case 6:
							book["binding"] = input("Enter the binding: ")
						case _:
							print("Invalid input.")
		case 4:
			type = input('''Search by:
1 - Title
2 - Author
3 - Publication year
4 - Genre

Enter a number: ''')

			match int(type):
				case 1:
					title = input("Enter the title: ")
					for book in books:
						if book["title"] == title:
							print(book)
				case 2:
					author = input("Enter the author: ")
					for book in books:
						if book["author"] == author:
							print(book)
				case 3:
					year = int(input("Enter the publication year: "))
					for book in books:
						if book["year"] == year:
							print(book)
				case 4:
					genre = input("Enter the genre: ")
					for book in books:
						if book["genre"] == genre:
							print(book)
				case _:
					print("Invalid input.")
		case _:
			print("Invalid input.")
