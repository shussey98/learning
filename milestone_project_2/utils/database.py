"""
Storing and retrieving books from a csv.
"""

books_file = 'books.txt'
def add_book(name, author):
    with open('books.txt','a') as file:
        file.write(f'{name},{author},0')
    books.append({'name': name, 'author': author, 'read': False})


