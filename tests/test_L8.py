# ruff: noqa: N999 -- Course task IDs require uppercase filenames used by check.py.
import copy
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL8(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.reading_list(EXAMPLE, 2020), [EXAMPLE[0]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.reading_list(list(reversed(EXAMPLE)), 2022), [EXAMPLE[0], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.reading_list(EXAMPLE, 1900), [])
        self.assertEqual(app.reading_list([], 2020), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

