class Book:
    def __init__(self, title, author, price, book_id):
        self.title = title
        self.author = author
        self.price = price
        self.book_id = book_id
        self.available = True
        self.borrowed_by = None

    def __repr__(self):
        return f"Book({self.title}, ID={self.book_id})"

    def borrow(self, member):
        if self.available :
            self.available = False
            self.borrowed_by = member 
        else:
            raise Exception(f"The book {self.title} is currently not available for borrowing.")

    def return_book(self, member):
        if self.available:
            raise Exception(f"The book {self.title} is not currently borrowed.")
        elif self.borrowed_by == member:
            self.available = True
            self.borrowed_by = None
        else:
            raise Exception(f"The book {self.title} was not borrowed by {member.name}.")


class Member:
    def __init__(self, name, member_id, member_contact):
        self.name = name
        self.member_id = member_id
        self.member_contact = member_contact
        self.borrowed_books = [] 
    def __repr__(self):
        return f"Member({self.name}, ID={self.member_id})"

    # def __eq__(self, other):
    #     return self.book_id == other.book_id
    
    def get_info(self):
        return f"Member Name : {self.name}, Member ID : {self.member_id}, Member Contact : {self.member_contact}, Borrowed Books : {[book.title for book in self.borrowed_books]}"
    
    def add_borrowed_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            raise Exception(f"{self.name} has already borrowed the book {book.title}.")  

    def remove_borrowed_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book) 
        else:
            raise Exception(f"{self.name} has not borrowed the book {book.title}.")  


class Library:
    def __init__(self,opening_time, closing_time):
        self.books = []
        self.members = []
        self.opening_time = opening_time
        self.closing_time = closing_time


    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                raise Exception(f"The book with ID {book.book_id} is already in the Library.")
        else:
            self.books.append(book)
        
    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                raise Exception(f"The member with ID {member.member_id} is already registered in the Library.")
        else:
            self.members.append(member)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        raise Exception(f"The Book with ID {book_id} is not found in the Library.")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise Exception (f"The Member with ID {member_id} is not found in the Library.")

    def borrow_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        book.borrow(member)
        member.add_borrowed_book(book) 

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        book.return_book(member)
        member.remove_borrowed_book(book)

try:
        
    library = Library("9:00 AM", "5:00 PM")

    book1 = Book("Atomic Habits", "James Clear", 500, 101)
    book2 = Book("Python", "Eric", 400, 102)

    member1 = Member("Joe", 1001, 1234567890)
    member2 = Member("Alice", 1002, 9876543210)

    library.add_book(book1)
    library.add_book(book2)
    library.add_member(member1)
    library.add_member(member2)
    library.borrow_book(101, 1001)
    library.return_book(101, 1001)
    library.return_book(101, 1003)
    library.borrow_book(102, 1002)
    print(library.books)
    print(library.members)
    print(member2.borrowed_books)


except Exception as e:
    print(e) 

print(book2.available)