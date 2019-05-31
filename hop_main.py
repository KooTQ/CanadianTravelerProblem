from data_structure.data_loading import usca312_data_loader
from heuristics_and_algorithms.probability_functions import upper_random as func
from heuristics_and_algorithms.HindsightOptimization import hindsight_optimization
from data_structure.HopNode import HopNode

start_index = 0
finish_index = 1
size = 30
N = int(2*(size**0.5))


def main():
    nodes = usca312_data_loader.load_nodes(func, size, HopNode)
    start = nodes[start_index]
    finish = nodes[finish_index]
    start.cost_to_come = 0
    result = hindsight_optimization(start, finish, N)

    print(result[0])
    print(result[1])


if __name__ == '__main__':
    main()

# End of file
