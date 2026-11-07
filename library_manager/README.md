# Campus Library Manager

This program keeps track of books, magazines and DVDs borrowed by library members.
It checks whether an item is available, limits how many items a member can borrow,
and calculates a late fee when an item is returned.

## Running the program

You need Python 3.12 or later. No extra packages are needed.
From the `library_manager` folder, run:

```sh
python3 main.py
```

On Windows, use `py -3 main.py` with Python 3.12 or later.
The demo uses Alice and Bob to show successful borrowing and returns, followed by
some deliberate mistakes. Messages such as "Could not borrow" are expected:
they show that the program catches the errors and keeps running.

## What is in this folder?

- `models.py` contains the item classes and the `Member` class.
- `main.py` runs the examples.
- `output.txt` contains the output from running the demo.
- `README.md` explains the program and answers the reflection questions below.

The starter code used `init` for the constructors. These are corrected to
`__init__` so Python calls them when objects are created.

Books cost Rs 2 per late day, magazines cost Rs 1, and DVDs cost Rs 5.
For three days, the fees are Rs 6, Rs 3 and Rs 15. A return on time costs Rs 0.
Alice has the default limit of three items, while Bob has a limit of one.

The program also checks for blank names, invalid IDs and negative or fractional
days. IDs, limits, issue numbers and durations must be positive whole numbers;
days late can be zero. Boolean values are not accepted as numbers.
A return with invalid days leaves the item on the member's borrowed list.

To save a fresh copy of the output, run:

```sh
python3 main.py > output.txt
```

The saved output was checked using Python 3.14.5.

## Reflection questions

### 1. Why is LibraryItem abstract, and what happens if DVD forgets late_fee()?

`LibraryItem` holds the behaviour that all items share, but each item type needs
its own late fee. Making `late_fee()` abstract means the child classes must
implement it. Creating a `LibraryItem` directly raises `TypeError`, and creating
a `DVD` would do the same if it did not implement `late_fee()`.

### 2. What happens when reading item.__available, and why use is_available()?

Reading `item.__available` outside the class raises `AttributeError` because
Python changes the internal name of a double-underscore attribute.
`is_available()` gives us a simple way to read that value, while the borrow and
return methods handle changes to it. This helps prevent accidental changes;
it is not a security feature that makes access impossible.

### 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` belongs to the class and is shared by books, magazines
and DVDs, so it counts the items created during that run.
`self.title` belongs to one item, so each book, magazine or DVD can have its own title.

## A couple of details

`borrowed_titles()` returns a new list of titles. Changing that list does not
change what the member has borrowed, as the demo shows.
Use `Member.borrow()` and `Member.return_item()` to keep the borrowed list and
availability in step; the item mark methods are included as required by the brief.
The data is kept in memory and disappears when the program stops.
There is no central catalogue to check for duplicate item IDs.
