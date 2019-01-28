from expression import Expression
from gene import Gene
import random

#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.open_file = open(self.file, "r")
        self.lines = self.open_file.readlines()


class Genetic_Algorithm(object):
    def __init__(self):
        self.population = []
        self.parser = Parser("algorithm.txt")
        self.generation = 1
        self.is_finished = False
        self.values = []
        self.info_file = open("info_file.txt", "w")

        #reads the expression
        for line in self.parser.lines:
            self.expression = Expression(line)

    def show_info(self):
        self.info_file.write('Finished?:' + str(self.is_finished) + '\n')


    #generates the population
    def gen_population(self, size):
        population = []
        for i in range(0, size, 1):
            g = Gene("")
            g.gen_gene(size)
            population.append(g)
        return population

    def run_algorithm(self, expression):
        while 


        
    