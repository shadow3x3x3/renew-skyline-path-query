class MultiAttributeGraph:
    """
    Record Basic Graph Data.
    Include Multi-Attribute edges.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.attributes = {}
        self.neighbors = {}

    def init_from_edges(self, edges):
        """
        Initialize form edges.
        When edges read, add nodes automatic from edges.
        """
        self.edges = tuple(edges)
        self.__init_nodes_from_edges()
        self.__init_neighbors()
        self.__init_attrs()

    def replace_nodes(self, new_nodes):
        self.nodes = new_nodes
        self.neighbors.clear()
        self.__init_neighbors()

    def find_paths(self, src, dst):
        """
        Find all possible paths without cycles.
        """
        return self._path_recursive(src, dst)

    def attrs_between(self, node1, node2):
        return self.attributes.get((node1, node2),
                                   self.attributes.get((node2, node1)))

    def _path_recursive(self, cur, dst, path=None):
        if path is None:
            path = []
        path = path + [cur]
        if cur == dst:
            return [path]
        paths = []
        for neighbor in self.neighbors[cur] - set(path):
            newpaths = self._path_recursive(neighbor, dst, path)
            for newpath in newpaths:
                paths.append(newpath)
        return paths

    def __init_nodes_from_edges(self):
        for edge in self.edges:
            if edge.src not in self.nodes:
                self.nodes.add(edge.src)
            if edge.dst not in self.nodes:
                self.nodes.add(edge.dst)

    def __init_neighbors(self):
        for node in self.nodes:
            self.neighbors[node] = self.__find_neighbors_by(node)

    def __find_neighbors_by(self, node):
        result = set()
        for edge in self.edges:
            if edge.dst in self.nodes and edge.src == node:
                result.add(edge.dst)
            if edge.src in self.nodes and edge.dst == node:
                result.add(edge.src)
        return result

    def __init_attrs(self):
        for edge in self.edges:
            self.attributes[edge.connect_nodes()] = edge.attrs
