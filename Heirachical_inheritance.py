# Hierarchical Inheritance: Library Management System

class LibraryItem:

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display_details(self):
        print("\n----- Library Item -----")
        print("Title:", self.title)
        print("Item ID:", self.item_id)

class Book(LibraryItem):

    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display_book(self):
        self.display_details()
        print("Author:", self.author)
        print("Pages:", self.pages)


class Magazine(LibraryItem):

    def __init__(self, title, item_id, issue_no, month):
        super().__init__(title, item_id)
        self.issue_no = issue_no
        self.month = month

    def display_magazine(self):
        self.display_details()
        print("Issue Number:", self.issue_no)
        print("Month:", self.month)



print("===== LIBRARY MANAGEMENT SYSTEM =====")

print("\n1. Add Book")

book_title = input("Enter book title: ")
book_id = input("Enter book ID: ")
author = input("Enter author name: ")
pages = int(input("Enter number of pages: "))

book = Book(book_title, book_id, author, pages)


print("\n2. Add Magazine")

magazine_title = input("Enter magazine title: ")
magazine_id = input("Enter magazine ID: ")
issue_no = input("Enter issue number: ")
month = input("Enter publication month: ")

magazine = Magazine(
    magazine_title,
    magazine_id,
    issue_no,
    month
)

print("\n BOOK DETAILS:")
book.display_book()
print("\n MAGAZINE DETAILS:")
magazine.display_magazine()