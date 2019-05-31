import sys
import operator
from data_structure.OptimisticNode import OptimisticNode
from data_structure.HopEdge import HopEdge

max_value = 1e9


class HopNode(OptimisticNode):
    def __init__(self, name, index, staying_cost=sys.float_info.max, sorting_edges_type="used_amount"):
        super().__init__(name, index, staying_cost)
        self.sorting_edges_type = sorting_edges_type
        self.generated_edges = None

    def add_edge(self, node, distance, probability):
        edge = HopEdge(node, distance, probability)
        if all(map(lambda a: a.get_end_node() != edge.get_end_node(), self.edges)):
            self.edges.append(edge)
        else:
            print("Already connected!")

    def get_currently_viable_edges(self, prev_node=None):
        if self.generated_edges is None:
            viable_edges = super().get_currently_viable_edges(prev_node)
            self.generated_edges = sorted(viable_edges, key=operator.attrgetter(self.sorting_edges_type))
        else:
            self.generated_edges = sorted(self.generated_edges, key=operator.attrgetter(self.sorting_edges_type))

        return self.generated_edges

    def get_edges(self):
        return self.get_currently_viable_edges()

    def reset(self):
        super().reset()
        self.generated_edges = None

    def reset_edges(self):
        for edge in self.edges:
            edge.reset()


# end of file
