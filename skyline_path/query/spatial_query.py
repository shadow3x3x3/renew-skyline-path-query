from skyline_path.algorithms.dijkstra import Dijkstra
from skyline_path.algorithms.dijkstra_heap import calculate_distances
from skyline_path.query.skyline_query import skyline_query

# params query_nodes_data: {nodes: values}
class SpatialQuery:
    def __init__(self, mag, target_edges):
        self.graph = mag
        self.target_edges = target_edges

    def query(self, src, dst):
        return skyline_query(self._spatial_values(src, dst))

    def _spatial_values(self, src, dst):
        spatial_nodes = {}
        for edge in self.target_edges:
            values = []
            nodes = edge.connect_nodes
            d = edge.dynamic_attr
            edge_dist = edge.distance

            src_node_path, src_dist = calculate_distances(self.graph, nodes[0], src)
            dst_node_path, dst_dist = calculate_distances(self.graph, nodes[0], dst)

            if src_dist and dst_dist:
                if src_dist > dst_dist: # we get dst to node0 and src to node1 here
                    src_node_path, src_dist = calculate_distances(self.graph, nodes[1], src)
                    values = [src_dist, dst_dist]
                else:                   # we get dst to node1 and src to node0 here
                    dst_node_path, dst_dist = calculate_distances(self.graph, nodes[1], dst)
                    values = [src_dist, dst_dist]
            full_path = src_node_path[::-1] + dst_node_path
            spatial_nodes[edge] = [values, full_path]
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
