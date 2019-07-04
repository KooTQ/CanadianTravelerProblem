import random


class Chromosome:
    def __init__(self, node, initial_genes_heuristic, mutate_chance):
        self.node = node
        self.genes = initial_genes_heuristic(node.output_edges)
        self.mutate_chance = mutate_chance
        self.mutate()

    def cross(self, other):
        if other.node != self.node:
            raise Exception("Trying to cross different chromosomes!")
        new_genes = []
        for i in range(len(self.genes)//2):
            new_genes.append(self.genes[i])
        for gene in other.genes:
            if gene not in new_genes:
                new_genes.append(gene)
        result = Chromosome(self.node, (lambda a: []), self.mutate_chance)
        result.genes = new_genes
        return result

    def mutate(self):
        for i in range(len(self.genes) - 1):
            roll = random.random()
            if self.mutate_chance >= roll:
                swap_ind = random.randint(0, len(self.genes) - 2)
                if swap_ind >= i:
                    swap_ind += 1
                self.swap(i, swap_ind)

    def swap(self, index1, index2):
        temp = self.genes[index1]
        self.genes[index1] = self.genes[index2]
        self.genes[index2] = temp

# tournament!
# End of file
