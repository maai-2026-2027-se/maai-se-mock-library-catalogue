import unittest

import app


class TestISBNFormatting(unittest.TestCase):
    def test_spaces_and_hyphens_are_removed_anywhere(self):
        self.assertEqual(app.normalize_isbn(' 0 8044-2957-x -'), '080442957X')

    def test_other_whitespace_and_unicode_digits_are_rejected(self):
        for value in ['0123456789\n', '01234\t56789', '\u00a00123456789',
                      '012345678\u0669', '\u0660123456789012']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                app.normalize_isbn(value)

    def test_checksum_is_not_validated(self):
        for value in ['0000000001', '0000000000001']:
            with self.subTest(value=value):
                self.assertEqual(app.normalize_isbn(value), value)
