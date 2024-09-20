def add_book(list_of_books: list, current_book):
    if current_book not in list_of_books:
        list_of_books.insert(0, current_book)
    return list_of_books


def take_book(list_of_books: list, current_book):
    if current_book in list_of_books:
        list_of_books.remove(current_book)
    return list_of_books


def swap_books(list_of_books: list, first_book, second_book):
    if first_book in list_of_books and second_book in list_of_books:
        index_first_book = list_of_books.index(first_book)
        index_second_book = list_of_books.index(second_book)
        list_of_books.remove(second_book)
        list_of_books.insert(index_second_book, first_book)
        list_of_books.remove(first_book)
        list_of_books.insert(index_first_book, second_book)
    return list_of_books


def insert_book(list_of_books: list, current_book):
    if current_book not in list_of_books:
        list_of_books.append(current_book)
    return list_of_books


def check_book(list_of_books: list, index: int):
    if index in range(len(list_of_books)):
        print("".join(list_of_books[index]))
    return list_of_books


books = input().split("&")
command = input()
while command != "Done":
    command = command.split(" | ")
    action = command[0]

    if action == "Add Book":
        book_name = command[1]
        books = add_book(books, book_name)
    elif action == "Take Book":
        book_name = command[1]
        books = take_book(books, book_name)
    elif action == "Swap Books":
        book_one = command[1]
        book_two = command[2]
        books = swap_books(books, book_one, book_two)
    elif action == "Insert Book":
        book_name = command[1]
        books = insert_book(books, book_name)
    elif action == "Check Book":
        book_index = int(command[1])
        books = check_book(books, book_index)

    command = input()

print(*books, sep=", ")
