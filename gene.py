import random

class Gene():
    def __init__(self, values):
        self.values = values

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