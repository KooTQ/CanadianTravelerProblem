import operator
import random

from heuristics_and_algorithms.path_finding import first


def random_shuffle(edges):
    result_genes = edges
    random.shuffle(result_genes)
    return result_genes


def shortest_first(edges):
    return sorted(edges, key=operator.attrgetter('cost'))


def longest_first(edges):
    return sorted(edges, key=operator.attrgetter('cost'), reverse=True)


def rollout_eval_with_fails(rollout, individual):
    current_start = rollout.start
    visited_nodes = [current_start]
    visited_edges = []
    while rollout.finish not in visited_nodes:
        current_chromosome = first(individual.chromosomes, key=(lambda a: a.node == current_start))
        best_edge = first(current_chromosome.genes, key=(lambda a: a.is_traversable()))
        visited_edges.append(best_edge)
        next_move = best_edge.end
        if next_move in visited_nodes:
            return None
        current_start = next_move
        visited_nodes.append(next_move)
    return sum(list(map((lambda a: a.cost), visited_edges)))

# find chromosome corresponding to current_start
# get next move
# set result as move destination
# if result is in visited return fail
# else add to visited and set as next current start
# repeat


def select_random_items(elems, size):
    shuffled = elems[:]
    random.shuffle(shuffled)
    return shuffled[0:size]

# End of file
