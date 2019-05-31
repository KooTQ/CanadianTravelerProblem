from data_structure.data_loading import usca312_data_loader
from heuristics_and_algorithms.probability_functions import upper_random as func
from heuristics_and_algorithms.Optimism import rechecking, keep_going
from data_structure.OptimisticNode import OptimisticNode

start_index = 0
finish_index = 1
size = 5


def main():
    nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
    start = nodes[start_index]
    finish = nodes[finish_index]
    start.cost_to_come = 0
    result = rechecking(start, finish)

    print(result[0])
    print(result[1])

    print("\n\n")
    nodes = usca312_data_loader.load_nodes(func, size, OptimisticNode)
    start = nodes[start_index]
    finish = nodes[finish_index]
    start.cost_to_come = 0
    result = keep_going(start, finish)

    print(result[0])
    print(result[1])


if __name__ == '__main__':
    main()

# End of file
