class Graph:
    """
    Record Basic Graph Data.
    """
    def __init__(self):
        self.nodes = ()

    def init_from_edges(self, edges):
        """
        Initialize form edges.
        When edges read, add nodes automatic from edges.
        """
        self.edges = tuple(edges)
        self.__init_nodes_from_edges()

    def __init_nodes_from_edges(self):
        for edge in self.edges:
            if edge.src not in self.nodes: self.nodes += (edge.src, )
            if edge.dst not in self.nodes: self.nodes += (edge.dst, )