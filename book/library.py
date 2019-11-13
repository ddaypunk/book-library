__name__ = "library"
__author__ = "andydelso"
"""Class definition for a library"""

from book.book import Book


class Library:
    books = []

    def addBook(self):
        # grab the info and create a new book in library list
        newBookTitle = str(raw_input("Title?: "))
        newBookPageCount = int(raw_input("Page Count?: "))
        newBookISBN = int(raw_input("ISBN?: "))

        self.books.append(Book(newBookTitle, newBookPageCount, newBookISBN, False))

    def printBooks(self):
        print "Book Title\t\t\t\t\t|  Page Count\t|  ISBN\t\t\t|  Status"
        print "----------------------------------------------------------------------"

        for each in self.books:
            print each.title,
            if len(each.title) > 13:
                print "\t\t\t| ",
            else:
                print "\t\t\t\t| ",
            print each.pageCount, "\t\t\t| ", each.isbn, "\t| ",
            if each.isOut == True:
                print "Out"
            else:
                print"In"