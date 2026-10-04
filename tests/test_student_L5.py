import copy
import unittest

import app


class TestStudentL5(unittest.TestCase):
    def test_sorts_by_year_then_casefolded_title(self):
        books = [
            {"title": "beta", "author": "Ada", "year": 2021, "available": True},
            {"title": "Zed", "author": "Lin", "year": 2019, "available": False},
            {"title": "Alpha", "author": "Ada", "year": 2021, "available": True},
        ]
        original = copy.deepcopy(books)
        self.assertEqual(app.sort_books(books), [books[1], books[2], books[0]])
        self.assertEqual(books, original)

    def test_ties_on_both_keys_keep_input_order(self):
        # "Git" and "GIT" casefold to the same key in the same year.
        books = [
            {"title": "Git", "author": "Ada", "year": 2020, "available": True},
            {"title": "GIT", "author": "Lin", "year": 2020, "available": False},
        ]
        result = app.sort_books(books)
        self.assertEqual([book["title"] for book in result], ["Git", "GIT"])
        self.assertIsNot(result, books)

    def test_empty_catalogue(self):
        self.assertEqual(app.sort_books([]), [])
