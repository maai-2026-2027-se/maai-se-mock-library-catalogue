import copy
import unittest

from app import find_books


class TestStudentL2(unittest.TestCase):
    def setUp(self):
        self.books = [
            {
                "title": "Python Basics",
                "author": "Ada",
                "year": 2020,
                "available": True,
            },
            {
                "title": "Learning Git",
                "author": "Python Club",
                "year": 2021,
                "available": False,
            },
            {
                "title": "Python Practice",
                "author": "Python Team",
                "year": 2022,
                "available": True,
            },
        ]

    def test_matches_title_or_author_once_in_input_order(self):
        original = copy.deepcopy(self.books)

        result = find_books(self.books, "  PYTHON  ")

        self.assertEqual(result, self.books)
        self.assertEqual(len(result), 3)
        self.assertEqual(self.books, original)

    def test_empty_or_whitespace_query_returns_all_books(self):
        for query in ("", "   ", "\t\n"):
            with self.subTest(query=query):
                self.assertEqual(find_books(self.books, query), self.books)

    def test_no_match_and_empty_catalogue(self):
        self.assertEqual(find_books(self.books, "missing"), [])
        self.assertEqual(find_books([], "python"), [])
