# Campus Library Manager

A small, in-memory Python assignment demonstrating abstraction, inheritance,
polymorphism, encapsulation, and exception handling. No external packages are needed.
All starter constructors have been corrected from `init` to `__init__`.

## Run

Use Python 3.12 or later. From this folder:

```sh
python3 --version
python3 main.py
```

On Windows use `py -3 main.py` with Python 3.12+ selected.
To regenerate the saved console transcript, run `python3 main.py > output.txt`.
The submitted output was captured using Python 3.14.5.

## Files and behaviour

- `models.py`: abstract `LibraryItem`, concrete `Book`, `Magazine`, `DVD`, and `Member`.
- `main.py`: two members, three items, normal borrowing/returns, caught errors,
  mixed-item fee calculations, abstract-class rejection, and private-state demonstrations.
- `output.txt`: the full output of the final demo run.

Books charge Rs 2/day, magazines Rs 1/day, and DVDs Rs 5/day; three days cost
Rs 6, Rs 3, and Rs 15 respectively. On-time returns cost Rs 0.
Members default to a three-item limit; Bob's one-item limit demonstrates rejection.
Titles and names must be non-empty strings; IDs, limits, issue numbers, and durations
must be positive integers; days late must be a non-negative integer. Booleans are
rejected as integer input. Invalid borrowing and return operations raise `ValueError`
with readable messages, and fee validation happens before any return state changes.

`borrowed_titles()` returns a fresh list, so modifying it cannot change the private
loan list. Python double underscores use name mangling to prevent accidental access;
they are not a security boundary. Use `Member.borrow()` and `Member.return_item()`
to keep the loan list and availability synchronized; the low-level mark methods
exist as required by the brief. This teaching example stores object references in
memory; it does not persist records or enforce a central catalogue of unique IDs.

## Reflection

### Why is LibraryItem abstract, and what if DVD forgets late_fee()?

`LibraryItem` defines common state and methods while requiring every concrete item
to provide its own late-fee calculation. Instantiating it raises `TypeError`; if
`DVD` omits `late_fee()`, DVD remains abstract and instantiating DVD also raises `TypeError`.

### What happens when reading item.__available, and why use is_available()?

Reading `item.__available` outside the class raises `AttributeError` because Python
mangles the attribute name inside `LibraryItem`. `is_available()` exposes the state
through a clear public method while changes go through the borrowing/return methods.

### How do LibraryItem.total_items and self.title differ?

`LibraryItem.total_items` is a class attribute shared across item types and counts
successfully constructed items during the current process. `self.title` is an
instance attribute belonging to one particular item, so different objects can have
different titles without changing each other's values.
