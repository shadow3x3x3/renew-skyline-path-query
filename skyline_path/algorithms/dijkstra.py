import math

class Dijkstra:
    """
    Find the shorest path with dimension
    """

    def __init__(self, graph, cache=None):
        self.graph = graph
        self.q = set()
        self.dist = dict.fromkeys(graph.nodes, math.inf)
        self.prev = dict.fromkeys(graph.nodes, None)
        self.cache = cache

    def shortest_path(self, src, dst):
        def get_path(src, dst):
            path = []
            vertext = dst
            while vertext is not None:
                path.append(vertext)
                vertext = self.prev[vertext]

            path.reverse()
            return path, self.dist[dst]

        if self._is_cache(src, dst):
            return get_path(src, dst)

        self.__init__(self.graph, src)
        q = self.q
        dist = self.dist
        prev = self.prev

        dist[src] = 0
        while q != self.graph.nodes:
            v = min((set(dist.keys() - q)), key=dist.get)
            for n in self.graph.neighbors[v] - q:
                next_attr = self.graph.attrs_between(v, n)
                if next_attr:
                    new_path = dist[v] + next_attr[0]
                if new_path < dist[n]:
                    dist[n] = new_path
                    prev[n] = v
                if dist[dst] != math.inf:
                    break
            q.add(v)

        return get_path(src, dst)

    def _is_cache(self, src, dst):
        return self.cache == src and self.dist[dst] != math.inf
