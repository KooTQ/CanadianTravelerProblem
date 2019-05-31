import sys
from data_structure.Node import Node
from data_structure.OptimisticEdge import OptimisticEdge

max_value = 1e9


class OptimisticNode(Node):
    def __init__(self, name, index, staying_cost=sys.float_info.max):
        super().__init__(name, index, staying_cost)
        self.cost_to_come = max_value
        self.staying_cost = staying_cost
        self.prev_node = None
        self.is_start = False

    def add_edge(self, node, distance, probability):
        edge = OptimisticEdge(node, distance, probability)
        if all(map(lambda a: a.get_end_node() != edge.get_end_node(), self.edges)):
            self.edges.append(edge)
        else:
            print("Already connected!")

    def reset(self):
        self.cost_to_come = max_value
        self.prev_node = None
        self.is_start = False

    def set_start(self):
        self.is_start = True
        self.cost_to_come = 0

# end of file
