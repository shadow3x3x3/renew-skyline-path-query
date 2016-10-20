class Edge:
    """
    Record Edge data
    """
    def __init__(self, id, src, dst, attrs):
        self.id = id
        self.src = src
        self.dst = dst
        self.distance = attrs[0] # Distane value on first position by default.
        self.attrs = attrs

    def connect_nodes(self):
        return (self.src, self.dst)
        