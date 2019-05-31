import operator


def dijkstra(finish, edges, viable_nodes):
    visited_nodes = []
    while viable_nodes:
        viable_nodes = get_sorted_nodes_by_cost_to_come(viable_nodes)
        current_node = viable_nodes[0]
        viable_nodes.remove(current_node)
        visited_nodes.append(current_node)
        if finish in visited_nodes:
            break
        if not current_node.is_start:
            edges = current_node.get_edges()
        for edge in edges:
            node = edge.get_end_node()
            if node in viable_nodes:
                old_cost = node.cost_to_come
                new_cost = current_node.cost_to_come + edge.get_weight()
                if old_cost > new_cost:
                    node.prev_node = current_node
                    node.cost_to_come = new_cost
    dijkstra_route = []
    dijkstra_route_node = finish
    while dijkstra_route_node.prev_node is not None:
        dijkstra_route.append(dijkstra_route_node)
        dijkstra_route_node = dijkstra_route_node.prev_node
    return dijkstra_route


def get_sorted_nodes_by_cost_to_come(nodes):
    return sorted(nodes, key=operator.attrgetter("cost_to_come"))


def get_nodes(start, start_edges, return_edges=False):
    result_nodes = []
    result_edges = []

    def inner(node, edges):
        result_nodes.append(node)
        for edge in edges:
            result_edges.append(edge)
            node = edge.get_end_node()
            if node not in result_nodes:
                inner(node, node.get_edges())

    inner(start, start_edges)
    if return_edges:
        return result_nodes, result_edges
    return result_nodes


def first(elements, key):
    for element in elements:
        if key(element):
            return element

# End of file
