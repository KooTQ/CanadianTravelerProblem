from data_structure.Edge import Edge


class HopEdge(Edge):
    def __init__(self, end_node, weight, probability):
        super().__init__(end_node, weight, probability)
        self.appeared_amount = 0
        self.used_amount = 0

    def reset(self):
        self.appeared_amount = 0
        self.used_amount = 0

    def appeared(self):
        self.appeared_amount = self.appeared_amount + 1

    def used(self):
        self.used_amount = self.used_amount + 1

# End of file
