from pprint import pprint
import sys
books = []

print("*********Please see below choices***********")

user_choice = """Enter: 
                - 'a' to add a new book,
                - 'd' to delete a book,
                - 'l' to list all books,
                - 'r' to mark a book as read
                - 'q' to quit

Your choice: """


def prompt_add_book():
    book_details = {}
    book_name = input("Please enter the name of the book: ")
    book_details["name"] = book_name
    book_author_name = input("Please enter the name of the author: ")
    book_details["author"] = book_author_name
    book_details["read"] = 'False'
    books.append(book_details)
    print(books)
    menu()


def list_books():
    pprint(books)
    menu()


""" This function changes the read flag to True if completed reading """


def prompt_read_book():
    book_name = input(
        "Please enter the name of the book you completed reading: ")
    for i in range(len(books)-1):
        if books[i]["name"] == book_name:
            books[i]["read"] = 'True'
    pprint(books)
    menu()


def prompt_delete_book():
    global books
    book_name = input("Please enter the name of the book you want to delete: ")
    books = [book for book in books if book['name'] != book_name]
    # for i in range(len(books) -1):
    #     if book_name not in books[i]['name']:
    #         print(f"Please add the book {book_name} in the repo first")
    # for i in range(len(books) -1):
    #     if books[i]['name'] == book_name:
    #         del books[i]
    #         print(f"The book {book_name} is deleted")
    #     pprint(books)

    menu()


menu_functions = {'a': prompt_add_book,
                  'd': prompt_delete_book,
                  'l': list_books,
                  'r': prompt_read_book}


def menu():
    user_input = input(user_choice)
    while user_input != 'q':
        try:
            function_call = menu_functions[user_input]
            function_call()
        except Exception as exc:
            print('me')
            print(exc)
            print("Please enter valid option")
            menu()
    sys.exit()


if __name__ == "__main__":

    menu()
