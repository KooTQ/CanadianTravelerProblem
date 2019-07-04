from data_structure.genetic_algorithm.EvaluationRollout import EvaluationRollout
from data_structure.genetic_algorithm.Individual import Individual
from data_structure.genetic_algorithm.heuristics import select_random_items

penalty = 10e4


class GeneticAlgorithm:
    def __init__(self, nodes, edges, start, finish, generations_amount, rollouts_amount, tournament_size,
                 population_amount, evaluation_func, mutation_chance, gene_initialization_heuristic):
        self.generations_amount = generations_amount
        self.tournament_size = tournament_size
        self.population_amount = population_amount
        self.rollouts_amount = rollouts_amount
        self.edges = edges
        self.nodes = nodes
        self.start = start
        self.finish = finish
        self.gene_init_heuristic = gene_initialization_heuristic
        self.mutation_chance = mutation_chance
        self.evaluation_func = evaluation_func
        self.evaluations = []
        self.population = []
        self.rollouts = []

    def create_initial_population(self):
        for i in range(self.population_amount):
            self.population.append(Individual(self.nodes, self.mutation_chance, self.gene_init_heuristic))

    def set_rollouts(self):
        if not self.rollouts:
            self.rollouts = list(EvaluationRollout(self.start, self.finish, self.nodes, self.edges)
                                 for _ in range(self.rollouts_amount))
        else:
            for rollout in self.rollouts:
                rollout.reset_all_nodes_dijkstra()
                rollout.reset_all_nodes_edges()

    def next_generation(self):
        self.set_rollouts()
        for indv in self.population:
            eval = list(self.evaluation_func(rollout, indv) for rollout in self.rollouts)
            if eval is None:
                eval = len(self.rollouts) * penalty
            tup = (eval, indv)
            self.evaluations.append(tup)

        new_population = []
        for _ in range(self.population_amount):
            first_min_tup = self.tournament()
            second_min_tup = self.tournament()
            new_population.append(Individual.cross(first_min_tup[1], second_min_tup[1]))
        self.population = new_population

    def tournament(self):
        selected = select_random_items(self.evaluations, self.tournament_size)
        min_tup = (len(self.rollouts) * penalty, None)
        for tup in selected:
            tup = (add_penalty(tup[0]), tup[1])
            avg = sum(tup[0]) / len(tup[0])
            if avg <= min_tup[0]:
                min_tup = (avg, tup[1])
        return min_tup


def add_penalty(arr):
    return list(map(lambda a: a if a is not None else penalty, arr))
# generate rollouts
#

# End of file
