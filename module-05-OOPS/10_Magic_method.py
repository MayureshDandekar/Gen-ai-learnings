# Magic Method

# class Book:
#     def __init__(self, book, author, pages ):
#         self.book = book
#         self.author = author
#         self.pages = pages

#     def info(self):
#         return f"{self.pages}"
#     # def __str__(self):
#     #     return f"{self.book} by {self.author}"
    

# book=Book("Atomic Habbits", "James Clear", 300)
# print(book)

































class Book:
    def __init__(self, book, author, pages):
        self.book = book
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.book} by {self.author}"
    def __repr__(self):
        return f"{self.book!r}, {self.author!r}, {self.pages!r}"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.pages == other.pages


book1 = Book("Atomic Habits", "James Clear", 300)
book2 = Book("Psychology of money", "Morgan Housel", 250)
# # print(book1)
# # print(str(book1))    # these are two ways to trigger/call the __str__ method automatically 
# # print(repr(book1))   # Trigger repr method
# # print(len(book1))      # Triger len method
# print(book1)
# print(book2)

str(book1)
repr(book1)
print(book1)