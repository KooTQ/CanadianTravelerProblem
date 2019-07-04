
class EvaluationRollout:
    def __init__(self, start, finish, nodes, edges):
        if start not in nodes:
            raise Exception("Start not in nodes")
        if finish not in nodes:
            raise Exception("Finish not in nodes")

        self.routes_per_edge = []
        self.start = start
        self.finish = finish
        self.edges = list(filter((lambda a: a.is_traversable()), edges))
        self.nodes = nodes

    def reset_all_nodes_edges(self):
        for node in self.nodes:
            node.reset_traversable_edges()
        self.edges = list(filter((lambda a: a.is_traversable()), self.edges))

    def reset_all_nodes_dijkstra(self):
        for node in self.nodes:
            node.reset_dijkstra()
        self.edges = list(filter((lambda a: a.is_traversable()), self.edges))

# End of file
