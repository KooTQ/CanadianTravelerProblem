
class Edge:
    def __init__(self, end_node, weight, probability):
        self.end_node = end_node
        self.weight = weight
        self.probability = probability

    def get_end_node(self):
        return self.end_node

    def get_weight(self):
        return self.weight

    def get_probability(self):
        return self.probability


# End of file
