# Library Catalogue: task pool

Each book is a dictionary with `title` (unique nonempty string), `author` (nonempty string), `year` (positive integer), and `available` (boolean). Assume well-formed records. Functions must not mutate their inputs; borrowing returns a new list of new dictionaries.

All nine tasks are required for final acceptance. Each function lives in `app.py`. Inputs follow the data model above unless a task explicitly asks for validation. Return values are checked for equality; object identity matters only where new dictionaries are required. Reuse requirements are checked by peer review.

For every task: add at least one meaningful test in `tests/test_student_<ID>.py`, run the task checks, create its completion marker, and open a PR. Round two also requires a regression demonstration. Round three also requires the shared release-note edit described in `CONTRIBUTING.md`.

## L1 — List available books

Round 1 · `available_books(books)`

Return available books in input order. Empty input returns `[]`.

No earlier task dependency.

Acceptance tests: `tests/test_L1.py`.

Run: `python3 check.py --task L1`; then `python3 check.py --complete L1`.

## L2 — Search titles and authors

Round 1 · `find_books(books, query)`

Strip and casefold the query and match it as a substring of the casefolded title or author. Preserve input order and include a book only once. Empty or whitespace-only query returns all books.

No earlier task dependency.

Acceptance tests: `tests/test_L2.py`.

Run: `python3 check.py --task L2`; then `python3 check.py --complete L2`.

## L3 — Count books by author

Round 1 · `author_counts(books)`

Return a dictionary mapping exact author labels to counts of all their books, including unavailable books. Empty input returns `{}`.

No earlier task dependency.

Acceptance tests: `tests/test_L3.py`.

Run: `python3 check.py --task L3`; then `python3 check.py --complete L3`.

## L4 — Fix borrowing without mutation

Round 2 · `borrow_book(books, title)`

Match an exact title. Return a new list of new dictionaries with that book's available field false; preserve order and all other fields. Raise `KeyError` if the title is absent, and `ValueError` if it is already unavailable. Preserve input even on failure.

No earlier task dependency.

Acceptance tests: `tests/test_L4.py`.

Run: `python3 check.py --task L4`; then `python3 check.py --complete L4`.

## L5 — Fix catalogue ordering

Round 2 · `sort_books(books)`

Return books sorted by year ascending, then casefolded title ascending. Preserve original order when both keys tie. Do not change the input list.

No earlier task dependency.

Acceptance tests: `tests/test_L5.py`.

Run: `python3 check.py --task L5`; then `python3 check.py --complete L5`.

## L6 — Fix ISBN formatting checks

Round 2 · `normalize_isbn(isbn)`

Remove ASCII spaces and hyphens; convert x to X. Accept either 13 ASCII digits or 10 characters with nine ASCII digits followed by an ASCII digit or X. Return the normalized string. Otherwise raise `ValueError`. This checks format only, not the ISBN checksum; other whitespace such as tabs is invalid. Assume a string input.

No earlier task dependency.

Acceptance tests: `tests/test_L6.py`.

Run: `python3 check.py --task L6`; then `python3 check.py --complete L6`.

## L7 — Build the lending report

Round 3 · `lending_report(books)`

Reuse `catalogue_size`, `available_books` and `author_counts`. Return exactly `total`, `available`, `borrowed` (counts), and `authors` (author counts). Empty input returns three zeros and `{}`.

Depends on: L1, L3, L4.

Acceptance tests: `tests/test_L7.py`.

Run: `python3 check.py --task L7`; then `python3 check.py --complete L7`.

## L8 — Build a reading list

Round 3 · `reading_list(books, maximum_year)`

Reuse `available_books` and `sort_books`. Return available books whose year is <= maximum_year, sorted by year then casefolded title. Assume an integer year; a year earlier than every book returns `[]`.

Depends on: L1, L5.

Acceptance tests: `tests/test_L8.py`.

Run: `python3 check.py --task L8`; then `python3 check.py --complete L8`.

## L9 — Export the catalogue to CSV

Round 3 · `to_csv(books)`

Return CSV with header `title,author,year,available`; encode available as 1 or 0. Preserve row order, use LF (`\n`) line endings including a final newline, and quote commas, quotes and embedded newlines with `csv`. Empty input returns the header plus newline.

No earlier task dependency.

Acceptance tests: `tests/test_L9.py`.

Run: `python3 check.py --task L9`; then `python3 check.py --complete L9`.
