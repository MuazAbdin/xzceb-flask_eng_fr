import unittest
from translator import english_to_french, french_to_english


class TestE2F(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')


class TestF2E(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
