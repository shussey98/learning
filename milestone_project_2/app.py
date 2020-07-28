from utils import database

USER_CHOICE ="""
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

Your choice:"""

def menu():
    user_input=input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            promt_read_book()
        elif user_input == 'd':
            promt_delete_book()
        user_input = input('Please input a choice from the menu: ')



def prompt_add_book():
    name = input('What is the name of your book?: ')
    author = input('Who is the authour of your book?: ')
    database.add_book(name, author)
    print(f'{name} by {author} has been added to your list')

def list_books():
    if len(database.books) > 0:
        for book in database.books:
            print(book['name']+', '+ book['author'])
    else:
        print('You have no books in your list!')


def promt_read_book():
    book = input('Which book have you read?: ')
    for item in database.books:
        if item['name'] == book:
            item['read'] = True

def promt_delete_book():
    book = input('Which book would you like to remove from your list?: ')
    for item in database.books:
        if item['name'] == book:
            database.books.remove(item)
    print(f'{book} has been removed from your list')


print(menu())
