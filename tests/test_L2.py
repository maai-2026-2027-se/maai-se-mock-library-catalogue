# ruff: noqa: N999 -- Course task IDs require uppercase filenames used by check.py.
import copy
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL2(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_books(EXAMPLE, '  ADA '), [EXAMPLE[0], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_books(EXAMPLE, 'IT'), [EXAMPLE[1]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_books(EXAMPLE, ' '), EXAMPLE)
        self.assertEqual(app.find_books(EXAMPLE, 'missing'), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        book = {'title': 'Straße', 'author': 'Straße', 'year': 2020, 'available': True}
        self.assertEqual(app.find_books([book], 'STRASSE'), [book])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

