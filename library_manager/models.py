"""Library items and members; requires Python 3.12+ and no packages."""
from abc import ABC, abstractmethod


def _text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string.")
    return value.strip()


def _integer(value, field, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{field} must be an integer of at least {minimum}.")
    return value


class LibraryItem(ABC):
    total_items = 0

    def __init__(self, title, item_id):
        self.title = _text(title, "Title")
        self.item_id = _integer(item_id, "Item ID")
        self.__available = True
        LibraryItem.total_items += 1

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        if not self.__available:
            raise ValueError(f"'{self.title}' is already borrowed.")
        self.__available = False

    def mark_returned(self):
        if self.__available:
            raise ValueError(f"'{self.title}' is already available.")
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        """Return a fee for a non-negative whole number of days."""


class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        self.author = _text(author, "Author")
        super().__init__(title, item_id)

    def late_fee(self, days_late):
        return _integer(days_late, "Days late", 0) * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


class Magazine(LibraryItem):
    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        self.issue_number = _integer(issue_number, "Issue number")
        super().__init__(title, item_id)

    def late_fee(self, days_late):
        return _integer(days_late, "Days late", 0) * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title}, issue {self.issue_number} (ID {self.item_id})"


class DVD(LibraryItem):
    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        self.duration_minutes = _integer(duration_minutes, "Duration in minutes")
        super().__init__(title, item_id)

    def late_fee(self, days_late):
        return _integer(days_late, "Days late", 0) * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title}, {self.duration_minutes} minutes (ID {self.item_id})"


class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = _text(name, "Member name")
        self.member_id = _integer(member_id, "Member ID")
        self.max_items = _integer(max_items, "Borrow limit")
        self.__borrowed = []

    @staticmethod
    def _validate_item(item):
        if not isinstance(item, LibraryItem):
            raise ValueError("Item must be a LibraryItem object.")

    def borrow(self, item):
        self._validate_item(item)
        if not item.is_available():
            raise ValueError(f"'{item.title}' is already borrowed.")
        if len(self.__borrowed) >= self.max_items:
            raise ValueError(f"{self.name} has reached the borrow limit ({self.max_items}).")
        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):
        self._validate_item(item)
        if item not in self.__borrowed:
            raise ValueError(f"{self.name} has not borrowed '{item.title}'.")
        # Validate the fee before changing either object's state.
        fee = item.late_fee(days_late)
        item.mark_returned()
        self.__borrowed.remove(item)
        return fee

    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]
