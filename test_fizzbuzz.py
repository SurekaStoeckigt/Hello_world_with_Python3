import unittest

from fizzbuzz import *

class FizzBuzzTests(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
        unittest.main()
