import unittest
from translator import english_to_french, french_to_english


class TestE2F(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(english_to_french('hello'), 'bonjour',
                         msg='E2F POSITIVE PASSED')

    def test_negative(self):
        self.assertNotEqual(english_to_french('hello'), 'merci',
                            msg='E2F NEGATIVE PASSED')


class TestF2E(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello',
                         msg='F2E POSITIVE PASSED')

    def test_negative(self):
        self.assertNotEqual(french_to_english('merci'), 'Hello',
                            msg='F2E NEGATIVE PASSED')


if __name__ == '__main__':
    unittest.main()
