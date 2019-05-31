from data_structure.Edge import Edge


class OptimisticEdge(Edge):
    def __init__(self, end_node, weight, probability):
        super().__init__(end_node, weight, probability)

    @property
    def cost_to_come(self):
        return self.get_end_node().cost_to_come

# End of file
