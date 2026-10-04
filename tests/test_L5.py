# ruff: noqa: N999 -- Course task IDs require uppercase filenames used by check.py.
import copy
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL5(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.sort_books(EXAMPLE), [EXAMPLE[1], EXAMPLE[0], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        books = [{'title': t, 'author': 'A', 'year': 2020, 'available': True} for t in ['z', 'A', 'a']]
        self.assertEqual(app.sort_books(books), [books[1], books[2], books[0]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        books = copy.deepcopy(EXAMPLE)
        app.sort_books(books)
        self.assertEqual(books, EXAMPLE)
        self.assertEqual(app.sort_books([]), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_year_takes_priority_over_title_and_titles_ignore_case(self):
        books = [
            {'title': 'Banana', 'author': 'A', 'year': 2021, 'available': True},
            {'title': 'Zebra', 'author': 'A', 'year': 1999, 'available': True},
            {'title': 'apple', 'author': 'A', 'year': 2021, 'available': True},
            {'title': 'Alpha', 'author': 'A', 'year': 2021, 'available': True},
        ]
        original = copy.deepcopy(books)
        self.assertEqual(app.sort_books(books), [books[1], books[3], books[2], books[0]])
        self.assertEqual(books, original)
