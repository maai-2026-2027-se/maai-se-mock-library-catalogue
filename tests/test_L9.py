import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Python', 'author': 'Ada', 'year': 2020, 'available': True}, {'title': 'Git', 'author': 'Lin', 'year': 2019, 'available': False}, {'title': 'Testing', 'author': 'Ada', 'year': 2022, 'available': True}]


class TestL9(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv([]), 'title,author,year,available\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv(EXAMPLE), 'title,author,year,available\nPython,Ada,2020,1\nGit,Lin,2019,0\nTesting,Ada,2022,1\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        books = [dict(title='A, B', author='C\"D\nE', year=2020, available=False)]
        self.assertEqual(list(csv.reader(io.StringIO(app.to_csv(books)))), [['title', 'author', 'year', 'available'], ['A, B', 'C\"D\nE', '2020', '0']])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

