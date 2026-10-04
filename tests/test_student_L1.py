import copy
import unittest

from app import available_books


class TestStudentL1(unittest.TestCase):
    def test_filters_books_preserving_order_and_input(self):
        books = [
            {"title": "Zebra", "author": "Ada", "year": 2020, "available": True},
            {"title": "Middle", "author": "Lin", "year": 2021, "available": False},
            {"title": "Apple", "author": "Ada", "year": 2022, "available": True},
        ]
        original = copy.deepcopy(books)

        self.assertEqual(available_books(books), [books[0], books[2]])
        self.assertEqual(books, original)

    def test_empty_input(self):
        self.assertEqual(available_books([]), [])