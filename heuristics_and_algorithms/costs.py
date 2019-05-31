from heuristics_and_algorithms.path_finding import first


def count_total_cost(final_route):
    total_cost = 0
    reset_all_nodes(final_route)
    for i in range(len(final_route) - 1):
        total_cost += first(
            final_route[i].get_edges(),
            (lambda a: a.get_end_node() == final_route[i + 1])
        ).get_weight()
    return total_cost


def reset_all_nodes(nodes):
    for resetting_node in nodes:
        resetting_node.reset()


# End of file
