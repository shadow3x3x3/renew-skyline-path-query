class RenewSelector:
    """
    Selecting Some Edges that need to be renew.
    By the sorting edges manager and distance.
    """

    def __init__(self, graph):
        self.postions = len(graph.edges)
        self.sort_edges = sorted(list(graph.edges), key=lambda e: e.dynamic_attr)

    def get_edges(self, nums):
        return self.sort_edges[:nums]

    def use_edges(self, edges):
        if not isinstance(edges, tuple):
            edges = (edges, )
        for e in edges:
            i = self.sort_edges.index(e)
            self.sort_edges.insert(self.postions, self.sort_edges.pop(i))