import math

class Dijkstra:
    """
    Find the shorest path with dimension
    """

    def __init__(self, graph):
        self.graph = graph
        self.q = set()
        self.dist = dict.fromkeys(graph.nodes, math.inf)
        self.prev = dict.fromkeys(graph.nodes, None)

    def shortest_path(self, src, dst):
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
            q.add(v)

        path = []
        vertext = dst
        while vertext is not None:
            path.append(vertext)
            vertext = prev[vertext]

        path.reverse()
        return path
