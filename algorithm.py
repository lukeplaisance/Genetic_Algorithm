from expression import Expression
from gene import Gene
import random

#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.read_file = open(self.file, "r")
        self.lines = self.read_file.readlines()


class Genetic_Algorithm(object):
    def __init__(self):
        self.population = []
        self.parser = Parser("algorithm.txt")
        self.generation = 1
        self.is_finished = False
        self.values = []
        self.info_file = open("info_file.txt", "w")

    def show_info(self):
        self.info_file.write('\n')
        self.info_file.write('Finished?:' + str(self.is_finished) + '\n')

    #generates the population
    def gen_population(self, size):
        population = []
        for i in range(0, size, 1):
            g = Gene("")
            g.gen_gene(size)
            population.append(g)
        return population

    #determines the fitness score
    def determine_fitness(self, expression):
        for gene in self.population:
            #the expression is assigned the original expression

    def run_algorithm(self, expression):
        gene_count = len(expression.get_variables())
        self.population = self.gen_population(gene_count)

        while not self.is_finished:
            print ('Generation: ' + str(self.generation))
            if(self.generation >= 500):
                self.show_info()
                return

def main():
    a = Genetic_Algorithm()
    p = Parser("algorithm.txt")
    #reads the expression
    for line in p.lines:
        e = Expression(line)

    a.run_algorithm(e)
    a.info_file.close()
    print ("finished")
main()


        
    