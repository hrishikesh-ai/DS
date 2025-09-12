class Student:
    def __init__(self, roll_no : int, name, std):
        self.name = name
        self.roll_no = roll_no
        self.std = std

    def showInfo(self):
        print(f"Student Name : {self.name}. \nRoll No.: {self.roll_no}. \n STD : {self.std}")

    def book_issue(self, book_obj):
        if book_obj.getStatus() == True:
            print(f"{self.name} has been Issued the book {book_obj.book_name}")
            book_obj.setStatus(False)
        else:
            print(f"The book {book_obj.book_name} is currently not available for {self.name}")

    def return_book(self, book_obj):
        book_obj.setStatus() == False
        print(f"The book {book_obj.book_name} has been returned Successfully")

class Book:
    def __init__(self, book_id : int, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.status = True

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

b1 = Book(101, "Harry Puttar", "Krish Diwakar")

s1 = Student(63, 'Amay Bihari', "5th Fail")
s2 = Student(17, 'Rohan Kumari', "2nd Fail")

s1.book_issue(b1)
s2.book_issue(b1)