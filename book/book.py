__name__ = "book"
__author__ = "andydelso"
"""Class definition for a book"""

class Book:
    def __init__(self, title, pageCount, isbn, isOut):
        self.title = title
        self.pageCount = pageCount
        self.isbn = isbn
        self.isOut = isOut

    def checkOut(self):
        self.isOut = True

    def checkIn(self):
        self.isOut = False

    def isCheckedOut(self):
        return self.isOut