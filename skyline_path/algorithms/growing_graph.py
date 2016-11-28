class GrowingGraph:
    def __init__(self, neighbors_table, start_nodes):
        self.neighbors_table = neighbors_table
        self.outer_nodes = set(start_nodes)
        self.inner_nodes = set()

    def growing(self):
        for old_node in self.outer_nodes.copy():
            self._update_nodes(old_node)

    def _update_nodes(self, old_node):
        new_nodes = set(self.neighbors_table[old_node])
        if new_nodes:
            self.outer_nodes.remove(old_node)
            self.inner_nodes.add(old_node)
            for new_node in new_nodes:
                if new_node not in self.inner_nodes:
                    self.outer_nodes.add(new_node)

    def __str__(self):
        return 'GrowingGraph(out:{}, in:{})'.format(
            self.outer_nodes, self.inner_nodes
        )

# testing
if __name__ == '__main__':
    neighbors_table = {
        1: (2, 3, 4, 5, 14),
        2: (1, 6, 7, 13),
        3: (1, 11, 12, 13),
        4: (1, 5, 8),
        5: (1, 4, 9, 10),
        6: (2, ),
        7: (2, ),
        8: (4, ),
        9: (5, ),
        10: (5, ),
        11: (3, ),
        12: (3, ),
        13: (2, 3),
        14: (1, )
    }

    gg = GrowingGraph(neighbors_table, [1, 2])
    print(gg)
    gg.growing()
    print(gg)
    gg.growing()
    print(gg)
    gg.growing()
    print(gg)
    gg.growing()
    print(gg)
