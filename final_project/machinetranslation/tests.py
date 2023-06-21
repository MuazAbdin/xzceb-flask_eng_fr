import unittest
from translator import english_to_french, french_to_english


class TestE2F(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'merci')



class TestF2E(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('merci'), 'Hello')

if __name__ == '__main__':
    unittest.main()
