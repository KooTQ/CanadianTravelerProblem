
from data_structure.data_loading.usca312_data_loader_hop import load_nodes
from data_structure.genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm
from heuristics_and_algorithms.probability_functions import lower_random as func
from data_structure.genetic_algorithm.heuristics \
    import rollout_eval_with_fails as eval_func, random_shuffle as init_func


def main():
    start_index = 0
    finish_index = 1
    size = 30

    nodes, edges = load_nodes(func, size)
    start = nodes[start_index]
    finish = nodes[finish_index]
    generation_amount = 10
    population_amount = 100
    rollouts = 20
    mutation_chance = 0.5
    tournament_size = 200

    ga = GeneticAlgorithm(nodes, edges, start, finish, generation_amount, rollouts, tournament_size,
                          population_amount, eval_func, mutation_chance, init_func)
    ga.create_initial_population()
    for i in range(generation_amount):
        ga.next_generation()
        evals = ga.evaluations
        selected = evals
        first_min_tup = (float('inf'), None)
        for tup in selected:
            if tup[0] is not None and sum(filter(lambda a: a is not None, tup[0]))/len(tup[0]) <= first_min_tup[0]:
                first_min_tup = (sum(filter(lambda a: a is not None, tup[0]))/len(tup[0]), tup[1])
        print(first_min_tup)


if __name__ == '__main__':
    main()
