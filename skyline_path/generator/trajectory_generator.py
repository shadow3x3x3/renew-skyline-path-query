import random

class TrajectoryGenerator:
    """
    Generating Trajectory by random.
    Include Graph.
    """

    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.trajectory = []

    def generator(self, prefer='value', stop_prob=1, sizes=10000):
        self.stop_prob = stop_prob
        self.trajectory.clear()
        self.find_random_paths(sizes)

    def find_random_paths(self, sizes):
        start_seed = len(self.graph.nodes) - 1

        while len(self.trajectory) < sizes:
            start_node = random.randrange(start_seed)
            self._path_recursive(start_node, random.randrange(2))

    def _path_recursive(self, cur, target, path=None):
        if path is None:
            path = []
        if len(path) >= 20:
            return
        path = path + [cur]
        if random.randrange(10) == self.stop_prob:
            self.trajectory.append(path)
            return
        next_ns = self.__next_node(cur, self.graph.neighbors[cur], target)
        for n in next_ns:
            if n not in path:
                self._path_recursive(n, target, path)
                return

    def __next_node(self, src, nodes, target):
        return self.__sort_nodes(src, nodes, target)[0:3]

    def __sort_nodes(self, src, nodes, target):
        nodes_attr = [self.graph.attrs_between(src, n)[target] for n in nodes]
        sorted_i = sorted(range(len(nodes_attr)), key=lambda k: nodes_attr[k])
        return [nodes[i] for i in sorted_i]