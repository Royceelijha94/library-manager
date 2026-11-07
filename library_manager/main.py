"""A short demo of borrowing, returning and handling mistakes."""
from models import Book, DVD, LibraryItem, Magazine, Member


def main():
    print("Campus Library Manager")
    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Science Today", 2, 42)
    dvd = DVD("Learning Python", 3, 90)
    items = [book, magazine, dvd]
    alice = Member("Alice", 101)
    bob = Member("Bob", 102, max_items=1)

    print("\nBorrowing items")
    try:
        alice.borrow(book)
        print("Alice borrowed:", book.describe())
        bob.borrow(book)
    except ValueError as e:
        print("Could not borrow:", e)
    try:
        alice.borrow(book)
    except ValueError as e:
        print("Trying to borrow the same book again:", e)
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

    print("\nLate fees for 3 days")
    # The same call uses the right fee for each item type.
    for item in items:
        print(item.describe(), "-> Rs", item.late_fee(3))
    print("Total items created:", LibraryItem.total_items)

    print("\nReturning items")
    try:
        alice.return_item(book, days_late=-1)
    except ValueError as e:
        print("Could not return:", e)
    print("Alice still has:", alice.borrowed_titles())
    try:
        print("Alice returned the book; fee: Rs", alice.return_item(book, 3))
        print("Bob returned the magazine on time; fee: Rs", bob.return_item(magazine))
        bob.borrow(dvd)
        print("Bob can now borrow the DVD because he returned the magazine.")
        print("Bob returned the DVD; fee: Rs", bob.return_item(dvd, 3))
    except ValueError as e:
        print("Could not complete this action:", e)
    try:
        bob.return_item(dvd)
    except ValueError as e:
        print("Trying to return the DVD again:", e)
    try:
        alice.borrow("not a library item")
    except ValueError as e:
        print("Could not borrow:", e)
    try:
        dvd.late_fee(1.5)
    except ValueError as e:
        print("Could not calculate the fee:", e)

    print("\nChecking the abstract class and private attributes")
    try:
        LibraryItem("x", 99)
    except TypeError:
        print("TypeError: Cannot create a LibraryItem directly because it is abstract.")
    try:
        print(book.__available)
    except AttributeError:
        print("AttributeError: Cannot read __available directly. Use is_available() instead.")
    try:
        print(alice.__borrowed)
    except AttributeError:
        print("AttributeError: Cannot read __borrowed directly. Use borrowed_titles() instead.")
    alice.borrow(book)
    # This is a copy, so clearing it should not change Alice's actual loans.
    titles = alice.borrowed_titles()
    titles.clear()
    print("After clearing the copy, Alice still has:", alice.borrowed_titles())
    alice.return_item(book)
    print("Is the book available now?", book.is_available())
    print("Alice's borrowed items:", alice.borrowed_titles())
    print("Bob's borrowed items:", bob.borrowed_titles())
    print("All items available:", all(item.is_available() for item in items))


if __name__ == "__main__":
    main()
