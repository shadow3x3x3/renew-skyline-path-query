import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algorithms.renew_selector import RenewSelector
from strcture.multi_attribute_graph import MultiAttributeGraph
from strcture.edge import Edge

E1 = Edge(0, 1, 2, [6])
E2 = Edge(1, 1, 2, [1])
E3 = Edge(2, 1, 2, [3])
E4 = Edge(3, 1, 2, [5])

class TestRenewSelector(unittest.TestCase):

    def setUp(self):
        mag = MultiAttributeGraph()
        mag.edges.add(E1)
        mag.edges.add(E2)
        mag.edges.add(E3)
        mag.edges.add(E4)
        self.rs = RenewSelector(mag)

    def test_init(self):
        first_edge = self.rs.sort_edges[0]
        second_edge = self.rs.sort_edges[1]
        third_edge = self.rs.sort_edges[2]
        fourth_edge = self.rs.sort_edges[3]
        self.assertEqual(first_edge, E2)
        self.assertEqual(second_edge, E3)
        self.assertEqual(third_edge, E4)
        self.assertEqual(fourth_edge, E1)

    def test_get_edges(self):
        get_edges = self.rs.get_edges(2)
        self.assertEqual(get_edges[0], E2)
        self.assertEqual(get_edges[1], E3)

    def test_use_edges(self):
        get_edges = self.rs.get_edges(2)
        self.rs.use_edges(get_edges[0])
        target_edge = self.rs.sort_edges[1]
        self.assertEqual(target_edge, E4)

if __name__ == '__main__':
    unittest.main()
