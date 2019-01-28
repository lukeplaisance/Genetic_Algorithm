import random

class Gene():
    def __init__(self, info):
        self.info = str(info)
        self.genes = []
        self.fitness = 0

    #generates a gene with randomly with numbers between 0 and 1
    def gen_gene(self, size):
        self.info = ""
        for i in range(0, size, 1):
            self.genes[i] = random.randint(0,1)
            self.info += str(self.genes[i])

    #determines the fitness score
    def determine_fitness(self):
        for value in self.genes:
            if self.genes[value] == 1:
                self.fitness += 1

    #gives each value in the gene a chance to flip it value
    def mutate(self, gene):
        mutated_gene = []
        mutation_chance = .25

        for i in gene:
            if random.random() < mutation_chance:
                if i == 1:
                    mutated_gene.append(0)
                else:
                    mutated_gene.append(1)
            else:
                mutated_gene.append(i)

        return mutated_gene

    #function that crosses over the ends of each gene to make a child gene
    def cross_over(self, geneOne, geneTwo, pivot):
        newGene = (geneOne[pivot:] + geneTwo[:pivot])
        return (newGene)