import operator

from data_structure.genetic_algorithm.Chromosome import Chromosome


class Individual:
    def __init__(self, nodes, mutation_chance, initial_genes_heuristic):
        self.initial_genes_heuristic = initial_genes_heuristic
        self.nodes = sorted(nodes, key=operator.attrgetter('index'))
        self.mutation_chance = mutation_chance
        self.chromosomes = list(Chromosome(node, self.initial_genes_heuristic, mutation_chance) for node in self.nodes)
        self.__hash = None
        self.costs = []

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def cross(self, other):
        result_indv = Individual(self.nodes, self.mutation_chance, (lambda a: []))
        result_chromosomes = []
        for i in range(len(self.chromosomes)):
            chromosome = self.chromosomes[i].cross(other.chromosomes[i])
            result_chromosomes.append(chromosome)
        result_indv.chromosomes = result_chromosomes
        result_indv.mutate()
        return result_indv

    def hash(self):
        if self.__hash is not None:
            return self.__hash
        self.__hash = 0
        amount_of_chromosomes = len(self.chromosomes)
        max_index_in_nodes = max(map((lambda a: a.node.index), self.chromosomes))
        for i in range(amount_of_chromosomes):
            amount_of_genes = len(self.chromosomes[i].genes)
            for j in range(amount_of_genes):
                self.__hash += (max_index_in_nodes**i) * self.chromosomes[i].genes[j].end.index

# Rollouts generated for each generation!
# End of file
