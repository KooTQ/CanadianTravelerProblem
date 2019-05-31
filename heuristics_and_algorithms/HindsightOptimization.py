from heuristics_and_algorithms.path_finding import dijkstra, get_nodes, first
from heuristics_and_algorithms.costs import count_total_cost


time_out = 100


def hindsight_optimization(start, finish, rollouts_amount, max_jumps=time_out):
    for rollout in range(rollouts_amount):
        start.set_start()
        viable_nodes, edges = get_nodes(start, start.get_edges(), return_edges=True)
        for edge in edges:
            edge.appeared()
        if finish in viable_nodes:
            dijkstra_route = dijkstra(finish=finish, edges=edges, viable_nodes=viable_nodes)
            for i in range(len(dijkstra_route) - 1):
                edge = first(dijkstra_route[i].get_edges(), (lambda a: a.get_end_node() == dijkstra_route[i+1]))
                edge.used()
        else:
            print("Fail at rollout number: " + str(rollout))
        for node in viable_nodes:
            node.reset()
    return generate_final_route(start, finish, max_jumps)


def generate_final_route(start, finish, max_jumps):
    new_start = start
    final_route = [new_start]
    timer = 0
    while new_start != finish:
        if timer >= max_jumps:
            print('Not connected start to finish in: ' + str(max_jumps) + ' jumps.')
            return -1, final_route
        edge = new_start.get_edges()[0]
        new_start.reset()
        new_start = edge.get_end_node()
        final_route.append(new_start)
    total_cost = count_total_cost(final_route)
    return total_cost, final_route

# End of file
