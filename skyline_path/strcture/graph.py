class Graph:
    """
    Record Basic Graph Data.
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