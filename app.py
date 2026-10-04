"""Library Catalogue: a small standard-library-only teaching project."""
import csv  # noqa: F401 -- available for the round-three CSV task
import io  # noqa: F401 -- available for the round-three CSV task
import json


def catalogue_size(books):
    """Existing working behavior; preserve it while adding features."""
    return len(books)


def available_books(books):
    """Return available books in their original order."""
    result = []

    for book in books:
        if book["available"]:
            result.append(book)

    return result


def find_books(books, query):
    """L2: Search titles and authors. See TASKS.md for the complete contract."""
    query = query.strip().casefold()
    return [
        book
        for book in books
        if query in book["title"].casefold() or query in book["author"].casefold()
    ]


def author_counts(books):
    """L3: Count books by author. See TASKS.md for the complete contract."""
    counts = {}
    for book in books:
        author = book["author"]
        counts[author] = counts.get(author, 0) + 1
    return counts


def borrow_book(books, title):
    """L4: Fix borrowing without mutation. See TASKS.md for the complete contract."""
    for index, book in enumerate(books):
        if book['title'] == title:
            if not book['available']:
                raise ValueError(f"Book {title!r} is already unavailable")
            result = [dict(item) for item in books]
            result[index]['available'] = False
            return result
    raise KeyError(title)


def sort_books(books):
    """L5: Fix catalogue ordering. See TASKS.md for the complete contract."""
    return sorted(books, key=lambda book: (book['year'], book['title'].casefold()))


def normalize_isbn(isbn):
    """L6: Fix ISBN formatting checks. See TASKS.md for the complete contract."""
    normalized = isbn.replace(' ', '').replace('-', '').replace('x', 'X')
    if normalized.isascii():
        if len(normalized) == 13 and normalized.isdigit():
            return normalized
        if (len(normalized) == 10 and normalized[:9].isdigit()
                and normalized[-1] in '0123456789X'):
            return normalized
    raise ValueError("ISBN must contain 13 ASCII digits or 9 ASCII digits followed by a digit or X")


def lending_report(books):
    """L7: Build the lending report. See TASKS.md for the complete contract."""
    total = catalogue_size(books)
    available = len(available_books(books))
    return {
        'total': total,
        'available': available,
        'borrowed': total - available,
        'authors': author_counts(books),
    }


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
