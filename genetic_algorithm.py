import random

#class for holding the symbols, literals, and clauses for the expressions
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")", " "]
        self.clauses = expression.split("*")
        self.values= ['0','1','0','0','1','1']
        self.variables = []
        self.literals = []

        #putting each unique character in a list
        for character in expression:            
            if character not in self.symbols:
                self.variables.append(character)
                self.variables = list(set(self.variables))
                self.variables.sort()            
        print (self.variables)

        #mapping each unique character with a value
        mappedVariable = list(zip(self.variables, self.values))
        print (mappedVariable)

        #taking the characters in the expression and replacing them with their value
        ex = expression
        for lit in mappedVariable:
            ex = ex.replace(lit[0], lit[1])

        #replacing the symbols with operators, then evaluates the expression
        for character in ex:
            ex = ex.replace(self.symbols[0], "not ")
            ex = ex.replace(self.symbols[1], "or")
            ex = ex.replace(self.symbols[2], "and")
        print(eval(ex))
        print(ex)


#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.open_file = open(self.file, "r")
        self.lines = self.open_file.readlines()

p = Parser("algorithm.txt")
for line in p.lines:
    e = Expression(line)    

#gives each value in the gene a chance to flip it value
def mutate(gene):
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
def cross_over(geneOne, geneTwo, pivot):
    newGene = (geneOne[pivot:] + geneTwo[:pivot])
    return (newGene)




a = [0,1,1,0,1,0]
b = [1,1,0,0,0,1]
cross = cross_over(a, b, 3)
print(cross)
mut = mutate(cross)
print(mut)

