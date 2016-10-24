from functools import reduce

from skyline_path.core import SkylineStatus
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
        """
        Give src and dst (Both are Nodes in this Graph)
        Find out all of skyline paths by SkyPath Algorithm.
        """
        return self._path_recursive(src, dst)

    def _path_recursive(self, cur, dst, path=None):
        if path is None:
            path = []
        path = path + [cur]
        if cur == dst:
            self.__add_new_sp_check(path)
            return
        for neighbor in self.neighbors[cur]:
            if self.__next_hop(neighbor, path):
                self._path_recursive(neighbor, dst, path)

    def __next_hop(self, neighbor, path):
        if neighbor in path:
            return False
        target_attrs = self.__attrs_in(path + [neighbor])
        if self.__partial_dominace(path + [neighbor], target_attrs):
            return False
        elif self.__full_dominace(path + [neighbor], target_attrs):
            return False
        else:
            return True

    def __partial_dominace(self, path, target_attrs):
        existed_attrs = self.partial_sp.get((path[0], path[-1]))
        if existed_attrs is not None:
            check = dominate_check(existed_attrs, target_attrs)
            if check is SkylineStatus.DOMINATE:
                return True
            elif check is SkylineStatus.NON_DOMINATE:
                return False
        # Here means old partial are dominated and replace it.
        self.partial_sp[(path[0], path[-1])] = target_attrs
        return False

    def __full_dominace(self, path, target_attrs):
        for _, existed_attrs in self.full_sp.items():
           check = dominate_check(existed_attrs, target_attrs)
           if check is SkylineStatus.DOMINATE:
                return True
        return False

    def __add_new_sp_check(self, path):
        temp_attrs = self.__attrs_in(path)
        # should use copy full sp due to changed size during iteration
        for sp, existed_attrs in self.full_sp.copy().items():
            check = dominate_check(existed_attrs, temp_attrs)
            if check is SkylineStatus.DOMINATE:
                return
            elif check is SkylineStatus.BE_DOMINATED:
                self.full_sp.pop(sp)
        # Check finished, add the new skyline path.
        self.full_sp[tuple(path)] = temp_attrs

    def __attrs_in(self, path):
        edges_attrs = self.__edges_to_attrs(self.__split_to(path))
        return reduce(lambda a1, a2: aggregate(a1, a2), edges_attrs)

    def __split_to(self, path):
        return [(path[i], path[i+1]) for i in range(len(path[:-1]))]

    def __edges_to_attrs(self, edges):
        return map(lambda e: self._attrs_between(e[0], e[1]), edges)
