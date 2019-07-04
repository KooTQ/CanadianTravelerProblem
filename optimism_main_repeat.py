from data_structure.data_loading import usca312_data_loader
from heuristics_and_algorithms.probability_functions import lower_random as func
from heuristics_and_algorithms.Optimism import rechecking, keep_going
from random import randint
from data_structure.OptimisticNode import OptimisticNode
import numpy as np
import time


size = 100
repeat_each_amount = 15
pair_amount = 10
eps = 1e-6


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
    times_keep = []
    times_recheck = []
    pairs = [(32, 71), (0, 94), (92, 20), (45, 53), (8, 32), (77, 43), (49, 24), (44, 30), (12, 82), (48, 52)]

    for pair_index in range(len(pairs)):
        start_index, finish_index = pairs[pair_index]
        single_pair_results_keep = []
        single_pair_results_recheck = []
        single_pair_times_keep = []
        single_pair_times_recheck = []
        for repeat_index in range(repeat_each_amount):
            print("Route test number: " + str(pair_index + 1) + " of " + str(len(pairs)))
            print("Current Start index: " + str(start_index) + " \t\tCurrent Finish index: " + str(finish_index))
            print("Test number: " + str(repeat_index) + " of " + str(repeat_each_amount))
            nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
            start = nodes[start_index]
            finish = nodes[finish_index]
            start.cost_to_come = 0
            time_recheck_start = time.time()
            result = rechecking(start, finish)
            time_recheck = time.time() - time_recheck_start

            print(result[0])
            single_pair_results_recheck.append(result[0])
            single_pair_times_recheck.append(time_recheck)

            nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
            start = nodes[start_index]
            finish = nodes[finish_index]
            start.cost_to_come = 0
            time_keep_start = time.time()
            result = keep_going(start, finish)
            time_keep = time.time() - time_keep_start
            print(result[0])
            single_pair_results_keep.append(result[0])
            single_pair_times_keep.append(time_keep)
            print("\n\n")
        results_keep.append(single_pair_results_keep)
        results_recheck.append(single_pair_results_recheck)
        times_keep.append(single_pair_times_keep)
        times_recheck.append(single_pair_times_recheck)
    avg_keeps = []
    avg_rechecks = []
    for result in results_keep:
        avg_keep = 0
        counter = eps
        for res in result:
            if res > -1:
                avg_keep += res
                counter += 1
        avg_keeps.append(avg_keep/counter)
    for result in results_recheck:
        avg_recheck = 0
        counter = eps
        for res in result:
            if res > -1:
                avg_recheck += res
                counter += 1
        avg_rechecks.append(avg_recheck/counter)
    for i in range(len(avg_rechecks)):
        print("Recheck: " + ('%.2f' % avg_rechecks[i]) + "\t\tKeep: " + ('%.2f' % avg_keeps[i]) +
              "\t\tRecheck-Keep: " + ('%.2f' % (avg_rechecks[i] - avg_keeps[i])))
    arr_keeps = np.array(results_keep)
    arr_rechecks = np.array(results_recheck)
    plotting_arr = np.column_stack((arr_keeps, arr_rechecks))
    print("\n\n" + str(arr_keeps.shape))
    print("\n\n" + str(arr_rechecks.shape))
    print("\n\n" + str(plotting_arr.shape))
    print("Pairs:")
    print(pairs)
    print("Recheck:")
    print(results_recheck)
    print("Keep:")
    print(results_keep)

    avg_times_keep = []
    avg_times_recheck = []
    for i in range(len(results_keep)):
        avg_time = 0
        counter = eps
        for j in range(len(results_keep[i])):
            if results_keep[i][j] > -1:
                avg_time += times_keep[i][j]
        avg_times_keep.append(avg_time/counter)

    for i in range(len(results_recheck)):
        avg_time = 0
        counter = eps
        for j in range(len(results_recheck[i])):
            if results_recheck[i][j] > -1:
                avg_time += times_recheck[i][j]
        avg_times_recheck.append(avg_time / counter)

    print("Time keeps: ")
    print(times_keep)
    print("Time recheck: ")
    print(times_recheck)


if __name__ == '__main__':
    main()

# End of file
