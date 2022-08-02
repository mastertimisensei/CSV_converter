from csv_conveter import csv_converter, Error,t 
import unittest

class TestPerfectSum(unittest.TestCase):
    
    def test_turkey(self):
        csv = csv_converter("example.txt")
        self.assertEqual(csv,t)

    def test_regular_with_laststrike(self):
        csv = csv_converter("ex.txt")
        self.assertEqual(csv,1)

    def test_misses_till_last_two_frame(self):
        csv = csv_converter('rubbish.txt')
        self.assertEqual(csv,1)


if __name__ == '__main__':
    unittest.main()
