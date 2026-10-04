# ruff: noqa: N999 -- Course task IDs require uppercase filenames used by check.py.
import copy
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL6(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.normalize_isbn(' 978-0-13-468599-1 '), '9780134685991')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.normalize_isbn('0-8044-2957-x'), '080442957X')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.normalize_isbn('0123456789'), '0123456789')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        for value in ['', '123', 'X123456789', '978013468599X', '０１２３４５６７８９', '\t0123456789']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                app.normalize_isbn(value)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

