import unittest

from main import count_letters

class TestCountLetter(unittest.TestCase):
    def test_count_letters(self):
        count = count_letters('hello world!')
        self.assertEqual('2', count[0])
