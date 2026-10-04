import copy
import unittest

import app


class TestStudentL3(unittest.TestCase):
    def test_counts_exact_labels_including_unavailable(self):
        books = [
            {"title": "Python", "author": "Ada", "year": 2020, "available": True},
            {"title": "Git", "author": "ada", "year": 2019, "available": False},
            {"title": "Testing", "author": "Ada", "year": 2022, "available": False},
        ]
        original = copy.deepcopy(books)
        self.assertEqual(app.author_counts(books), {"Ada": 2, "ada": 1})
        self.assertEqual(books, original)

    def test_empty_catalogue(self):
        self.assertEqual(app.author_counts([]), {})
