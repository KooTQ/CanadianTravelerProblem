import sys
import numpy as np
from data_structure.Edge import Edge
from heuristics_and_algorithms.path_finding import first

max_value = 1e9


class Node:
    def __init__(self, name, index, staying_cost=sys.float_info.max):
        self.is_start = False
        self.name = name
        self.index = index
        self.output_edges = []
        self.staying_cost = staying_cost

    def get_currently_viable_edges(self, prev_node=None):
        viable_edges = []
        for edge in self.output_edges:
            rand_number = np.random.random_sample()
            if rand_number > edge.probability:
                viable_edges.append(edge)
        return viable_edges

    def add_edge(self, node, distance, probability):
        edge = Edge(node, distance, probability)
        if all(map(lambda a: a.get_end_node() != edge.get_end_node(), self.output_edges)):
            self.output_edges.append(edge)
        else:
            print("Already connected!")

    def get_edges(self):
        if self.is_start:
            return self.get_currently_viable_edges()
        else:
            return self.output_edges

    def get_all_edges(self):
        return self.output_edges

    def get_name(self):
        return self.name

    def get_nodes(self):
        nodes = map((lambda a: a.get_end_node()), self.get_edges())
        return nodes

    def copy_without_edges(self, node_type):
        copy = node_type(self.name, self.index, self.staying_cost)
        return copy

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __repr__(self):
        return str(self.index) + "\t" + self.name


def deep_copy_nodes(start, finish, nodes_type=None):
    old_nodes = [start]
    new_nodes = []

    def generate_inner_nodes(edges, prev):
        for c_edge in edges:
            node = c_edge.get_end_node()
            if node not in old_nodes:
                old_nodes.append(node)
                generate_inner_nodes(node.get_currently_viable_edges(prev), node)
    generate_inner_nodes(start.get_all_edges(), None)

    for old_node in old_nodes:
        new_nodes.append(old_node.copy_without_edges(nodes_type))

    for i in range(len(old_nodes)):
        for edge in old_nodes[i].get_all_edges():
            end_node = first(new_nodes, (lambda a: a == edge.get_end_node()))
            new_nodes[i].add_edge(end_node, edge.get_weight(), edge.get_probability())

    new_start = first(new_nodes, (lambda a: a == start))
    new_finish = first(new_nodes, (lambda a: a == finish))
    return new_start, new_finish

# end of file
