import unittest
import sys
sys.path.insert(0, './testing')
from my_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
if __name__ == '__main__':
    unittest.main()


# python -m unittest test
# python -m unittest -v test


# This will search the current directory for any files named test*.py and attempt to test them.
# python -m unittest discovers

# unittest will run all tests in a single test plan and give you the results.
# python -m unittest discover -s tests

# unittest will change to the src/ directory, 
# scan for all test*.py files inside the the tests directory, and execute them.
#  python -m unittest discover -s tests -t src