import operator

from heuristics_and_algorithms.path_finding import first


def get_all_connected_nodes(start):
    all_nodes = [start]

    def inner(edges):
        for edge in edges:
            if edge.end not in all_nodes:
                all_nodes.append(edge.end)
                inner(edge.end.get_traversable_edges())

    inner(start.get_traversable_edges())
    return all_nodes


class HopRoute:
    def __init__(self):
        self.route = []
        self.costs_to_get_to_corresponding_node = []

    def add_node_to_route(self, node):
        if len(self.route) == 0:
            self.route.append(node)
            self.costs_to_get_to_corresponding_node.append(0)
        else:
            edge = first(self.route[len(self.route) - 1].output_edges, (lambda a: a.end == node))
            self.route.append(node)
            self.costs_to_get_to_corresponding_node.append(edge.cost)

    @property
    def full_cost(self):
        return sum(self.costs_to_get_to_corresponding_node)

    @staticmethod
    def find_route(start_edge, finish):
        start = start_edge.end
        start.cost_to_come = 0
        viable_nodes = get_all_connected_nodes(start)
        visited_nodes = []
        if finish not in viable_nodes:
            print("\t\tFinish not connected to start in HopRoute.find_route" + str((start, finish)))
            return None

        while viable_nodes:
            current_node = first(
                sorted(viable_nodes, key=operator.attrgetter('cost_to_come')),
                (lambda a: a not in visited_nodes))
            viable_nodes.remove(current_node)
            visited_nodes.append(current_node)
            sorted_edges = sorted(current_node.get_traversable_edges(), key=operator.attrgetter("cost"))
            for edge in sorted_edges:
                node = edge.end
                old_cost = node.cost_to_come
                new_cost = current_node.cost_to_come + edge.cost
                if old_cost > new_cost:
                    node.prev_dijkstra = current_node
                    node.cost_to_come = new_cost
        route = []
        dijkstra_route_node = finish
        while dijkstra_route_node.prev_dijkstra is not None:
            route.append(dijkstra_route_node)
            dijkstra_route_node = dijkstra_route_node.prev_dijkstra
        route.reverse()
        result = HopRoute()
        for node in route:
            result.add_node_to_route(node)

        return result

    def get_full_cost(self):
        return sum(self.costs_to_get_to_corresponding_node)
# End of file
