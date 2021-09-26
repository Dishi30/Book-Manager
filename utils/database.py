import sqlite3


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO books VALUES(?,?,0)', (name, author))
    connection.commit()
    connection.close()


def get_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()

    return books


def readed(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
    connection.commit()
    connection.close()


def delete(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connection.commit()
    connection.close()






bfile = 'books.txt'


def create_book_table():
    with open(bfile, 'w'):
        pass


def add_book(name, author):
    with open(bfile, 'a') as file:
        file.write(f"{name},{author},0\n")


def get_books():
    with open(bfile, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]


def readed(name):
    books = get_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_books(books)


def _save_books(books):
    with open(bfile, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete(name):
    books = get_books()
    books = (book for book in books if book['name'] != name)
    _save_books(books)

# def delete(name):
#  for book in books:
#     if book['name'] == name:
#        books.remove(book)
