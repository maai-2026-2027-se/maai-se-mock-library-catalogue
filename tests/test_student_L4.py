# The lab requires the uppercase task ID in this test filename.
# ruff: noqa: N999
import copy
import unittest

import app

BOOKS = [
    {"title": "Python", "author": "Ada", "year": 2020, "available": True},
    {"title": "Git", "author": "Lin", "year": 2019, "available": False},
    {"title": "Testing", "author": "Ada", "year": 2022, "available": True},
]


class TestStudentL4(unittest.TestCase):
    def test_success_returns_new_records_without_changing_input(self):
        books = copy.deepcopy(BOOKS)
        original = copy.deepcopy(books)

        result = app.borrow_book(books, "Testing")

        expected = copy.deepcopy(BOOKS)
        expected[2]["available"] = False
        self.assertIsNot(result, books)
        self.assertEqual(result, expected)
        self.assertEqual(books, original)
        for source, borrowed in zip(books, result):
            self.assertIsNot(borrowed, source)

    def test_missing_title_raises_and_preserves_input(self):
        books = copy.deepcopy(BOOKS)
        original = copy.deepcopy(books)

        with self.assertRaises(KeyError):
            app.borrow_book(books, "Missing")

        self.assertEqual(books, original)

    def test_unavailable_title_raises_and_preserves_input(self):
        books = copy.deepcopy(BOOKS)
        original = copy.deepcopy(books)

        with self.assertRaises(ValueError):
            app.borrow_book(books, "Git")

        self.assertEqual(books, original)
