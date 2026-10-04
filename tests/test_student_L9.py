# ruff: noqa: N999 -- Task IDs in filenames are required by check.py.
import copy
import csv
import io
import unittest

import app


class TestCSVExport(unittest.TestCase):
    def test_special_characters_preserve_order_and_input(self):
        books = [
            {'title': 'Z, "last"\nline', 'author': 'Zoë',
             'year': 2024, 'available': False},
            {'title': 'A', 'author': 'First, "second"\nthird',
             'year': 1999, 'available': True},
        ]
        original = copy.deepcopy(books)

        result = app.to_csv(books)

        self.assertEqual(
            result,
            'title,author,year,available\n'
            '"Z, ""last""\nline",Zoë,2024,0\n'
            'A,"First, ""second""\nthird",1999,1\n',
        )
        self.assertEqual(list(csv.reader(io.StringIO(result))), [
            ['title', 'author', 'year', 'available'],
            ['Z, "last"\nline', 'Zoë', '2024', '0'],
            ['A', 'First, "second"\nthird', '1999', '1'],
        ])
        self.assertEqual(books, original)

    def test_empty_catalogue_has_header_and_final_newline(self):
        self.assertEqual(app.to_csv([]), 'title,author,year,available\n')
