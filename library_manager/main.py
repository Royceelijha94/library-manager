"""Run the campus library demonstration with: python3 main.py."""
from models import Book, DVD, LibraryItem, Magazine, Member


def main():
    print("CAMPUS LIBRARY MANAGER")
    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Science Today", 2, 42)
    dvd = DVD("Learning Python", 3, 90)
    items = [book, magazine, dvd]
    alice = Member("Alice", 101)
    bob = Member("Bob", 102, max_items=1)

    print("\nBorrowing and errors")
    try:
        alice.borrow(book)
        print("Alice borrowed:", book.describe())
        bob.borrow(book)
    except ValueError as e:
        print("Could not borrow:", e)
    try:
        alice.borrow(book)
    except ValueError as e:
        print("Duplicate borrowing refused:", e)
    try:
        bob.borrow(magazine)
        print("Bob borrowed:", magazine.describe())
        bob.borrow(dvd)
    except ValueError as e:
        print("Could not borrow:", e)
    try:
        bob.return_item(book)
    except ValueError as e:
        print("Could not return:", e)

    print("\nPolymorphism: late fees for 3 days")
    for item in items:
        print(item.describe(), "-> Rs", item.late_fee(3))
    print("Total items created:", LibraryItem.total_items)

    print("\nValidation and returns")
    try:
        alice.return_item(book, days_late=-1)
    except ValueError as e:
        print("Invalid return refused:", e)
    print("Alice still holds the book:", alice.borrowed_titles())
    try:
        print("Alice returned the book; fee: Rs", alice.return_item(book, 3))
        print("Bob returned the magazine on time; fee: Rs", bob.return_item(magazine))
        bob.borrow(dvd)
        print("Bob borrowed the DVD after freeing a slot.")
        print("Bob returned the DVD; fee: Rs", bob.return_item(dvd, 3))
    except ValueError as e:
        print("Library action failed:", e)
    try:
        bob.return_item(dvd)
    except ValueError as e:
        print("Repeated return refused:", e)
    try:
        alice.borrow("not a library item")
    except ValueError as e:
        print("Invalid item refused:", e)
    try:
        dvd.late_fee(1.5)
    except ValueError as e:
        print("Invalid days refused:", e)

    print("\nAbstraction and encapsulation")
    try:
        LibraryItem("x", 99)
    except TypeError:
        print("TypeError: LibraryItem is abstract and cannot be instantiated.")
    try:
        print(book.__available)
    except AttributeError:
        print("AttributeError: __available is private; use is_available().")
    try:
        print(alice.__borrowed)
    except AttributeError:
        print("AttributeError: __borrowed is private; use borrowed_titles().")
    alice.borrow(book)
    titles = alice.borrowed_titles()
    titles.clear()
    print("Clearing a returned titles list leaves Alice's loans intact:", alice.borrowed_titles())
    alice.return_item(book)
    print("Book available via is_available():", book.is_available())
    print("Alice's final loans:", alice.borrowed_titles())
    print("Bob's final loans:", bob.borrowed_titles())
    print("All items available:", all(item.is_available() for item in items))


if __name__ == "__main__":
    main()
