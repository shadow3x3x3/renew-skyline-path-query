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

    def attrs(self, index = None):
        if index is None:
            return self.attrs
        else:
            return self.attrs[index]