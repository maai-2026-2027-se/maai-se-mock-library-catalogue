import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestBaseline(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.catalogue_size([]), 0)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.catalogue_size(EXAMPLE), 3)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

