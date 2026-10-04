"""Library Catalogue: a small standard-library-only teaching project."""
import csv  # noqa: F401 -- available for the round-three CSV task
import io  # noqa: F401 -- available for the round-three CSV task
import json


def catalogue_size(books):
    """Existing working behavior; preserve it while adding features."""
    return len(books)


def available_books(books):
    """L1: List available books. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L1: List available books")


def find_books(books, query):
    """L2: Search titles and authors. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L2: Search titles and authors")


def author_counts(books):
    """L3: Count books by author. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L3: Count books by author")


def borrow_book(books, title):
    """L4: Fix borrowing without mutation. See TASKS.md for the complete contract."""
    for book in books:
        if book['title'] == title:
            book['available'] = False
    return books


def sort_books(books):
    """L5: Fix catalogue ordering. See TASKS.md for the complete contract."""
    return sorted(books, key=lambda book: (book['year'], book['title'].casefold()))


def normalize_isbn(isbn):
    """L6: Fix ISBN formatting checks. See TASKS.md for the complete contract."""
    return isbn.replace('-', '')


def lending_report(books):
    """L7: Build the lending report. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L7: Build the lending report")


def reading_list(books, maximum_year):
    """L8: Build a reading list. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L8: Build a reading list")


def to_csv(books):
    """L9: Export the catalogue to CSV. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement L9: Export the catalogue to CSV")


if __name__ == "__main__":
    example = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]
    print(json.dumps(example, indent=2))
    print("catalogue_size:", catalogue_size(example))
