__author__ = 'andydelso'

from book.library import Library
from book.book import Book

library = Library()

#the following and book library included for testing
library.books.append(Book("Wizard of Oz", 92, 1495421864, False))
library.books.append(Book("Off to be a Wizard", 386, 1612184715, False))
library.books.append(Book("The Alchemist", 197, 0061122416, False))


#library.addBook()
#library.addBook()
#library.addBook()

library.books[1].checkOut()

library.printBooks()

#book1 = Book("Wizard of Oz", 100, 1234567, False)

#if __name__ == '__main__':