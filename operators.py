import random
from gene import Gene

#gives each value in the gene a chance to flip it value
def mutate(gene):
    mutated_gene = []
    mutation_chance = .25

    for i in gene.info:
        if random.random() < mutation_chance:
            if i == 1:
                mutated_gene.append(0)
            else:
                mutated_gene.append(1)
        else:
            mutated_gene.append(i)

    return mutated_gene

#function that crosses over the ends of each gene to make a child gene
def cross_over(geneOne, geneTwo, pivot):
    g1 = ""
    g2 = ""
    for i in range(0, pivot):
        g1 += str(geneOne.info[i])
        g2 += str(geneTwo.info[i])

    for i in range(pivot, len(geneOne.info)):
        g1 += str(geneTwo.info[i])
        g2 += str(geneOne.info[i])

    g1 = Gene(g1)
    g2 = Gene(g2)
    return [g1,g2]

def select_parent(population):
    p1 = population[0]

    rand_parent = random.randint(1, len(population) - 1)
    p2 = population[rand_parent]
    new_population = [p1, p2]
    return new_population