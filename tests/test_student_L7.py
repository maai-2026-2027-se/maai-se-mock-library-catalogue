import copy
import unittest

import app


class TestStudentL7(unittest.TestCase):
    def test_counts_borrowed_books_and_all_authors(self):
        books = [
            {"title": "Python", "author": "Ada", "year": 2020, "available": False},
            {"title": "Git", "author": "Lin", "year": 2019, "available": False},
            {"title": "Testing", "author": "Ada", "year": 2022, "available": True},
        ]
        original = copy.deepcopy(books)
        self.assertEqual(
            app.lending_report(books),
            {"total": 3, "available": 1, "borrowed": 2, "authors": {"Ada": 2, "Lin": 1}},
        )
        self.assertEqual(books, original)

    def test_all_borrowed_still_counts_authors(self):
        books = [{"title": "Git", "author": "Lin", "year": 2019, "available": False}]
        self.assertEqual(
            app.lending_report(books),
            {"total": 1, "available": 0, "borrowed": 1, "authors": {"Lin": 1}},
        )

    def test_empty_catalogue(self):
        self.assertEqual(
            app.lending_report([]),
            {"total": 0, "available": 0, "borrowed": 0, "authors": {}},
        )
