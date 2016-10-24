from functools import reduce

from skyline_path.core.dominate import dominate_check
from skyline_path.strcture.multi_attribute_graph import MultiAttributeGraph
from skyline_path.core.edge_helper import aggregate

class SkyPath(MultiAttributeGraph):
    """
    Implement SkyPath Algorithm.
    Inherit from MultiAttributeGraph
    """
    def __init__(self):
        super().__init__()
        # record partial skyline paths and full skyline paths
        # with their attributes
        self.partial_sp = {}
        self.full_sp = {}

    def skypath_query(self, src, dst):
        # TODO return self._path_recursive(src, dst)

    def _path_recursive(self, cur, dst, path=[]):
        path = path + [cur]
        if cur == dst:
            return [path]
        paths = []
        for neighbor in self.neighbors[cur]:
            if self.__next_hop(neighbor, path):
                newpaths = self._path_recursive(neighbor, dst, path)
                for newpath in newpaths:
                    paths.append(newpath)
            else:
                return paths
        return paths

    def __next_hop(self, neighbor, path):
        if neighbor in path:
            return False
        elif self.__partial_dominace(path):
            return False
        elif self.__full_dominace(path):
            return False
        else:
            return True

    def __partial_dominace(self, path):
        # TODO: partial path dominace check
        self.partial_sp[[path[0], path[-1]]] = self.__attrs_in(path)

    def __full_dominace(self, path):
        # TODO: full path dominace check
        pass

    def __attrs_in(self, path):
        edges_attrs = self.__edges_to_attrs(self.__split_to(path))
        return reduce(lambda a1, a2: aggregate(a1, a2), edges_attrs)

    def __split_to(self, path):
        return [(path[i], path[i+1]) for i in range(len(path[:-1]))]

    def __edges_to_attrs(self, edges):
        return map(lambda e: self._attrs_between(e[0], e[1]), edges)
