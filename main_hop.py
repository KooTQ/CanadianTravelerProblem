from random import randint

from data_structure.data_loading.usca312_data_loader_hop import load_nodes
from heuristics_and_algorithms.probability_functions import lower_random as func
from data_structure.HopRollout import HopRollout
from heuristics_and_algorithms.HindsightOptimization import HindsightOptimization
import numpy as np
import matplotlib.pyplot as plt

pair_amount = 2
size = 100
N = 10
repeat = 10


def create_indices_set():
    pairs = []

    for _ in range(pair_amount):
        start_index = randint(0, size - 1)
        finish_index = randint(0, size - 1)
        if start_index == finish_index:
            finish_index = (finish_index + 1) % size
        pair = (start_index, finish_index)
        pairs.append(pair)
    return pairs


def main():
    pairs = [(32, 71), (0, 94)]
    # , (92, 20), (45, 53), (8, 32), (77, 43), (49, 24), (44, 30), (12, 82), (48, 52)]
    costs_hop = []
    times_prep_hop = []
    times_decision_hop = []
    for pair in pairs:
        start_index, finish_index = pair
        nodes, edges = load_nodes(func, size)
        start = nodes[start_index]
        finish = nodes[finish_index]
        results = []
        single_pair_costs_hop = []
        single_pair_times_prep_hop = []
        single_pair_times_decision_hop = []
        for i in range(repeat):
            print("\nExperiment number: " + str(i) + " pair: " + str(pair))
            hop = HindsightOptimization(N, nodes, edges, start, finish)
            result = hop.hindsight_optimization_runner()
            cost, path, prep_time, decision_time = result
            single_pair_costs_hop.append(cost)
            single_pair_times_prep_hop.append(prep_time)
            single_pair_times_decision_hop.append(decision_time)
            print("Results: ")
            print(cost, path)
            results.append(result)
        costs_hop.append(single_pair_costs_hop)
        times_prep_hop.append(single_pair_times_prep_hop)
        times_decision_hop.append(single_pair_times_decision_hop)
    print('Costs: ')
    print(costs_hop)
    print('Prep Time: ')
    print(times_prep_hop)
    print('Decision Time:')
    print(times_decision_hop)


if __name__ == '__main__':
    main()

# End of file
