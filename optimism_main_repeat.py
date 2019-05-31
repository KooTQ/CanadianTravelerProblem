from data_structure.data_loading import usca312_data_loader
from heuristics_and_algorithms.probability_functions import upper_random as func
from heuristics_and_algorithms.Optimism import rechecking, keep_going
from random import randint
from data_structure.OptimisticNode import OptimisticNode

size = 15
repeat_each_amount = 50
pair_amount = 15


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
    results_keep = []
    results_recheck = []
    pairs = create_indices_set()

    for pair_index in range(len(pairs)):
        start_index, finish_index = pairs[pair_index]
        single_pair_results_keep = []
        single_pair_results_recheck = []
        for repeat_index in range(repeat_each_amount):
            print("Route test number: " + str(pair_index) + " of " + str(len(pairs)))
            print("Current Start index: " + str(start_index) + " \t\tCurrent Finish index: " + str(finish_index))
            print("Test number: " + str(repeat_index) + " of " + str(repeat_each_amount))
            nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
            start = nodes[start_index]
            finish = nodes[finish_index]
            start.cost_to_come = 0
            result = rechecking(start, finish)

            print(result[0])
            single_pair_results_recheck.append(result)

            nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
            start = nodes[start_index]
            finish = nodes[finish_index]
            start.cost_to_come = 0
            result = keep_going(start, finish)
            print(result[0])
            single_pair_results_keep.append(result)
            print("\n\n")
        results_keep.append(single_pair_results_keep)
        results_recheck.append(single_pair_results_recheck)
    avg_keeps = []
    avg_rechecks = []
    for result in results_keep:
        avg_keep = 0
        for res, _ in result:
            avg_keep += res / len(result)
        avg_keeps.append(avg_keep)
    for result in results_recheck:
        avg_recheck = 0
        for res, _ in result:
            avg_recheck += res / len(result)
        avg_rechecks.append(avg_recheck)

    for i in range(len(avg_rechecks)):
        print("Recheck: " + str(avg_rechecks[i]) + "\t\tKeep: " + str(avg_keeps[i]) +
              "\t\tRecheck-Keep: " + str(avg_rechecks[i] - avg_keeps[i]))


if __name__ == '__main__':
    main()

# End of file
