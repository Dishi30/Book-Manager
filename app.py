from utils import database

user_choice = """
Enter:
-'a' to ADD new book
-'l' to LIST all book
-'r' to mark a book as READ
-'d' to DELETE a book
-'q' to QUIT

Your choice: """


def menu():
    database.create_book_table()
    a = input(user_choice)
    while a != 'q':
        if a == 'a':
            add()
        elif a == 'l':
            list_book()
        elif a == 'r':
            read_book()
        elif a == 'd':
            del_book()
        else:
            print("UNKNOWN COMMAND, please try again")

        a = input(user_choice)


def add():
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")

    database.add_book(name, author)


def list_book():
    books = database.get_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read : {read}")


def read_book():
    name = input("Enter the name of book you just finished reading: ")
    database.readed(name)


def del_book():
    name = input("Enter the book you want to delete: ")
    database.delete(name)


menu()
