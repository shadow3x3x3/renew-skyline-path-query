import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from skyline_path.core import SkylineStatus
from skyline_path.core.dominate import dominate_check

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

class TestSkylineDominate(unittest.TestCase):

    def setUp(self):
        pass

    def test_skyline_dominate_result(self):
        self.assertEqual(dominate_check(d[1], d[2]), SkylineStatus.DOMINATE)
        self.assertEqual(dominate_check(d[2], d[1]), SkylineStatus.BE_DOMINATED)
        self.assertEqual(dominate_check(d[3], d[5]), SkylineStatus.NON_DOMINATE)
        self.assertEqual(dominate_check(d[5], d[3]), SkylineStatus.NON_DOMINATE)

if __name__ == '__main__':
    unittest.main()
