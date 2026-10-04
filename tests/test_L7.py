# ruff: noqa: N999 -- Course task IDs require uppercase filenames used by check.py.
import copy
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL7(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.lending_report(EXAMPLE), {'total': 3, 'available': 2, 'borrowed': 1, 'authors': {'Ada': 2, 'Lin': 1}})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.lending_report([]), {'total': 0, 'available': 0, 'borrowed': 0, 'authors': {}})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        borrowed = app.borrow_book(EXAMPLE, 'Python')
        self.assertEqual(app.lending_report(borrowed)['borrowed'], 2)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

