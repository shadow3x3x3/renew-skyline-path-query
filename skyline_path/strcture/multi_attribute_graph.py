class MultiAttributeGraph:
    """
    Record Basic Graph Data.
    Include Multi-Attribute edges.
    """
    def __init__(self):
        self.nodes = ()
        self.neighbors = {}

    def init_from_edges(self, edges):
        """
        Initialize form edges.
        When edges read, add nodes automatic from edges.
        """
        self.edges = tuple(edges)
        self.__init_nodes_from_edges()
        self.__init_neighbors()

    def find_paths(self, src, dst):
        return self._path_recursive(src, dst)

    def _path_recursive(self, cur, dst, path=[]):
        path = path + [cur]
        if cur == dst:
            return [path]
        paths = []
        for neighbor in self.neighbors[cur]:
            if neighbor not in path:
               newpaths = self._path_recursive(neighbor, dst, path)
               for newpath in newpaths:
                   paths.append(newpath)
        return paths

    def __init_nodes_from_edges(self):
        for edge in self.edges:
            if edge.src not in self.nodes: 
                self.nodes += (edge.src, )
            if edge.dst not in self.nodes: 
                self.nodes += (edge.dst, )
    
    def __init_neighbors(self):
        for node in self.nodes:
            self.neighbors[node] = self.__find_neighbors_by(node)

    def __find_neighbors_by(self, node):
        result = ()
        for edge in self.edges:
            if edge.src == node:
                result += (edge.dst, )
            if edge.dst == node:
                result += (edge.src, )
        return result