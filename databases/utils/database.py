import sqlite3
from typing import List,Dict

Book = Dict[str, Union[str,int]]

def create_book_table() -> None:
    connection =sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    connection.commit()
    connection.close()

def insert_book(name: str, author:str):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?,?, 0)', (name, author))
    connection.commit()
    connection.close()



def get_all_books() -> List[Book]:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # list of tuples
    connection.close()

    return books

def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name =?',(name,))
    connection.commit()

    connection.close()



def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name =?',(name,))
    connection.commit()

    connection.close()