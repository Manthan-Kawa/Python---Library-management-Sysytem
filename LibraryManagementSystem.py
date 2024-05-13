class Book:
    def __init__(self,id, title, author, year, status='Available'):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        # Define the spacing between attributes
        spacing = 5
        # Format the attributes with appropriate spacing
        return f"{self.id:<{spacing}}{self.title:<{spacing*3+3}}{self.author:<{spacing*5+2}}{self.year:<{spacing+2}}{self.status:<{spacing}}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added successfully!")

    def display_all_books(self):
        if self.books:
            print("All books in the library:")
            print("\n\n------------------------------------------------------------------------------")
            print("{:<4} {:<17} {:<18} {:<14} {}".format("ID", "Title", "Author", "Publish Year", "Status"))
            print("------------------------------------------------------------------------------")

            for book in self.books:
                print(book)

        else:
            print("No books available in the library.")
        print("------------------------------------------------------------------------------")    

    def display_available_books(self):
        available_books = [book for book in self.books if book.status == 'Available']
        if available_books:
            print("Available books in the library:")
            print("\n\n------------------------------------------------------------------------------")
            print("{:<4} {:<17} {:<18} {:<14} {}".format("ID", "Title", "Author", "Publish Year", "Status"))
            print("------------------------------------------------------------------------------")
            for book in available_books:
                print(book)
               
        else:
           print("------------------------------------------------------------------------------")           
           for book in self.books:
                print(book)
        print("------------------------------------------------------------------------------")                

    def borrow_book(self, book_id):
      for book in self.books:
        if book.id == book_id and book.status == 'Available':
            print("Book borrowed successfully!")
            book.status = 'Not Available'
            return
      print("No Book Available for Borrow with the given ID.")


    def return_book(self, book_id):
     for book in self.books:
        if book.id == book_id and book.status == 'Not Available':
            print("Book Returned successfully!")
            book.status = 'Available'
            return
        print("No Book Available for Return with the given ID.")

def main():
    library = Library()
    valid_username = "admin"
    valid_password = "password"

    entered_username = input("\nEnter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == valid_username and entered_password == valid_password:
        print("\nLogin Successful", entered_username, "!!")

        while True:
          print("\n\nWelcome To Library Management System "+ entered_username +"!!")
          print("\n1. Add Book")
          print("2. Show All Books")
          print("3. Show Available Books")
          print("4. Borrow Book")
          print("5. Return Book")
          print("6. Exit")

          choice = input("Enter your choice: ")

          if choice == '1':
            id = input("Enter Book Id : ")
            title = input("Enter Title Of The Book : ")
            author = input("Enter Author of the book: ")
            year = input("Enter Year of Publish: ")
            new_book = Book(id,title, author, year)
            library.add_book(new_book)
          elif choice == '2':
            library.display_all_books()
          elif choice == '3':
            library.display_available_books()
          elif choice == '4':
            book_id = input("Enter ID of the book you want to borrow: ")
            library.borrow_book(book_id)
          elif choice == '5':
            book_id = input("Enter ID of the book you want to return: ")
            library.return_book(book_id)
          elif choice == '6':
            print("\nTHANKS FOR USING OUR LIBRARY MANAGEMENT SYSTEM !!?\n")
            print("B021 - Manthan Kawa")
            print("B017 - Shivesh Hegde\n\n")
            break
          else:
            print("Invalid Choice !!")

    else:
        print("Login Failed "+entered_username)


if __name__ == "__main__":
    main()
