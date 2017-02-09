import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from skyline_path.query.skyline_query import skyline_query

d = {
    1: [1, 4],
    2: [5, 6],
    3: [9, 2],
    4: [7, 7],
    5: [6, 3]
}

s = {
    1: [1, 4],
    3: [9, 2],
    5: [6, 3]
}

class TestSkylineQuery(unittest.TestCase):

    def setUp(self):
        self.result = skyline_query(d)

    def test_skyline_query_result(self):
        self.assertEqual(len(self.result), 3)
        self.assertEqual(self.result, s)

if __name__ == '__main__':
    unittest.main()
