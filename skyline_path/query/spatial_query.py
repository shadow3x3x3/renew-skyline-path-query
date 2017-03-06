from skyline_path.algorithms.dijkstra import Dijkstra
from skyline_path.algorithms.dijkstra_heap import calculate_distances
from skyline_path.query.skyline_query import skyline_query

# params query_nodes_data: {nodes: values}
class SpatialQuery:
    def __init__(self, mag, target_edge):
        self.graph = mag
        self.target_edge = target_edge

    def query(self, src, dst):
        return skyline_query(self._spatial_values(src, dst))

    def _spatial_values(self, src, dst):
        spatial_nodes = {}
        for edge in self.target_edge:
            values = []
            nodes = edge.connect_nodes
            d = edge.dynamic_attr
            edge_dist = edge.distance
            v, path1 = self._calc_attributes(src, nodes, d, edge_dist)
            values.append(v)
            v, path2 = self._calc_attributes(dst, nodes, d, edge_dist)
            values.append(v)
            path2.reverse()
            path = path1 + path2
            spatial_nodes[edge] = [values, path]
        return spatial_nodes # { node ids: [value, path] }

    def _calc_attributes(self, query_node, nodes, d, edge_dist):
        path1, dist1 = calculate_distances(self.graph, query_node, nodes[0])
        path2, dist2 = calculate_distances(self.graph, query_node, nodes[1])

        if dist1 and dist2:
            if dist1 > dist2:
                return round(dist2/d, 4), path2
            else:
                return round(dist1/d, 4), path1
        else:
            return round(edge_dist/d, 4), [query_node]
