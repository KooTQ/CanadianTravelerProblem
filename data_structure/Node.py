import sys
import numpy as np

max_value = 1e9


class Node:
    def __init__(self, name, index, staying_cost=sys.float_info.max):
        self.edges = []
        self.name = name
        self.index = index
        self.staying_cost = staying_cost
        self.is_start = False

    def get_currently_viable_edges(self, prev_node=None):
        viable_edges = []
        for edge in self.edges:
            rand_number = np.random.random_sample()
            if rand_number < edge.probability:
                viable_edges.append(edge)
            elif prev_node is not None and prev_node == edge.end_node:
                viable_edges.append(edge)
        return viable_edges

    def get_edges(self):
        if self.is_start:
            return self.get_currently_viable_edges()
        else:
            return self.edges

    def get_name(self):
        return self.name

    def get_nodes(self):
        nodes = map((lambda a: a.get_end_node()), self.get_edges())
        return nodes

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __repr__(self):
        return str(self.index) + "\t" + self.name

# end of file
