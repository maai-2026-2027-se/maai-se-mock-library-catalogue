import copy
import unittest
from unittest.mock import patch

import app


class TestStudentL8(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"title": "Zebra", "author": "Ada", "year": 2020, "available": True},
            {"title": "Future", "author": "Lin", "year": 2021, "available": True},
            {"title": "Borrowed", "author": "Ada", "year": 2010, "available": False},
            {"title": "apple", "author": "Lin", "year": 2020, "available": True},
            {"title": "Old", "author": "Ada", "year": 2019, "available": True},
            {"title": "Banana", "author": "Lin", "year": 2020, "available": True},
        ]

    def test_filters_available_books_and_includes_cutoff_year(self):
        self.assertEqual(
            app.reading_list(self.books, 2020),
            [self.books[4], self.books[3], self.books[5], self.books[0]],
        )

    def test_orders_by_year_then_casefolded_title(self):
        self.assertEqual(
            [book["title"] for book in app.reading_list(self.books, 2021)],
            ["Old", "apple", "Banana", "Zebra", "Future"],
        )

    def test_empty_input_and_no_matching_year(self):
        self.assertEqual(app.reading_list([], 2020), [])
        self.assertEqual(app.reading_list(self.books, 1900), [])

    def test_all_unavailable_returns_empty(self):
        self.assertEqual(app.reading_list([self.books[2]], 2020), [])

    def test_input_order_and_records_are_unchanged(self):
        original = copy.deepcopy(self.books)
        for cutoff in (1900, 2020, 2021):
            with self.subTest(cutoff=cutoff):
                result = app.reading_list(self.books, cutoff)
                self.assertEqual(self.books, original)
                self.assertIsNot(result, self.books)

    def test_equal_sort_keys_preserve_input_order(self):
        books = [
            {"title": "apple", "author": "Ada", "year": 2020, "available": True},
            {"title": "APPLE", "author": "Lin", "year": 2020, "available": True},
        ]
        self.assertEqual(app.reading_list(books, 2020), books)

    def test_reuses_availability_and_sorting_helpers(self):
        with (
            patch.object(app, "available_books", wraps=app.available_books) as available,
            patch.object(app, "sort_books", wraps=app.sort_books) as sort,
        ):
            result = app.reading_list(self.books, 2020)
        available.assert_called_once_with(self.books)
        sort.assert_called_once_with(
            [self.books[0], self.books[3], self.books[4], self.books[5]]
        )
        self.assertEqual(
            result, [self.books[4], self.books[3], self.books[5], self.books[0]]
        )