import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL4(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        books = copy.deepcopy(EXAMPLE)
        result = app.borrow_book(books, 'Python')
        self.assertFalse(result[0]['available'])
        self.assertEqual(result[1:], EXAMPLE[1:])
        self.assertEqual(books, EXAMPLE)
        for before, after in zip(books, result):
            self.assertIsNot(before, after)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(KeyError):
            app.borrow_book(EXAMPLE, 'missing')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        books = copy.deepcopy(EXAMPLE)
        with self.assertRaises(ValueError):
            app.borrow_book(books, 'Git')
        self.assertEqual(books, EXAMPLE)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

