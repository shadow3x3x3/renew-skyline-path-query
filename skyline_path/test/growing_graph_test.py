import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithms.growing_graph import GrowingGraph
from strcture.multi_attribute_graph import MultiAttributeGraph

NEIGHTBORS_TABLE = {
    1: {2, 3, 4, 5, 14},
    2: {1, 6, 7, 13},
    3: {1, 11, 12, 13},
    4: {1, 5, 8},
    5: {1, 4, 9, 10},
    6: {2},
    7: {2},
    8: {4},
    9: {5},
    10: {5},
    11: {3},
    12: {3},
    13: {2, 3},
    14: {1}
}

class TestGrowingGraph(unittest.TestCase):

    def setUp(self):
        self.gg = GrowingGraph(NEIGHTBORS_TABLE, [1, 2])

    def test_init(self):
        init_outer = self.gg.outer_nodes
        init_inner = self.gg.inner_nodes
        self.assertEqual(init_outer, {1, 2})
        self.assertEqual(init_inner, set())

    def test_growing(self):
        self.gg.growing()
        init_outer = self.gg.outer_nodes
        init_inner = self.gg.inner_nodes
        self.assertEqual(init_outer, {3, 4, 5, 6, 7, 13, 14})
        self.assertEqual(init_inner, {1, 2})

if __name__ == '__main__':
    unittest.main()
