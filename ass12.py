
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")

    with open("books.txt", "a") as f:
        position = f.tell()
        f.write(book_id + "," + name + "\n")

    with open("index.txt", "a") as f:
        f.write(book_id + "," + str(position) + "\n")

    print("Book added successfully")


def search_book():
    book_id = input("Enter Book ID to search: ")

    found = False

    with open("index.txt", "r") as f:
        for line in f:
            bid, position = line.strip().split(",")

            if bid == book_id:
                with open("books.txt", "r") as book:
                    book.seek(int(position))
                    print("Book Record:", book.readline())

                found = True
                break

    if not found:
        print("Book not found")


while True:
    print("\n1.Add Book")
    print("2.Search Book")
    print("3.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_book()

    elif ch == 2:
        search_book()

    elif ch == 3:
        break

    else:
        print("Invalid choice")
