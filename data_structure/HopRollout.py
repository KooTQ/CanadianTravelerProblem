from data_structure.HopRoute import HopRoute


class HopRollout:
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

    def find_routes(self):
        if len(self.start.get_traversable_edges()) > 0:
            for edge in self.start.get_traversable_edges():
                route = HopRoute.find_route(edge, self.finish)
                if route is not None:
                    self.routes_per_edge.append(route)
                    self.reset_all_nodes_dijkstra()
                else:
                    print("Start and Finish are not connected in this rollout.\n")
                    break

    def reset_all_nodes_edges(self):
        for node in self.nodes:
            node.reset_traversable_edges()

    def reset_all_nodes_dijkstra(self):
        for node in self.nodes:
            node.reset_dijkstra()

# End of file
