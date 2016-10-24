from skyline_path.strcture.edge import Edge

def read_edges_data(file_path):
    """
    Reading text file by every line.
    Then let lines be a Edge()
    Line format: id src dst *attrs
    """
    edges = []
    for line in open(file_path, 'r', encoding='UTF-8'):
        # remove /n and split to string array
        # then making string array to int array
        raw_edge = list(map(float, line.rstrip().split(' ')))
        edges.append(
            Edge(raw_edge[0],
                 raw_edge[1],
                 raw_edge[2],
                 raw_edge[3:])
            )
    return edges