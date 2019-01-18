from expression import Expression
from gene import Gene
import random

#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.open_file = open(self.file, "r")
        self.lines = self.open_file.readlines()


class Genetic_Algorithm():
    def __init__(self, expression):
        self.population = []
        self.parser = Parser("algorithm.txt")
        self.expression = expression

        for line in self.parser.lines:
            self.expression = Expression(line)

    def gen_population(self, size):
        for i in range(0, size):
            values = []
        for j in self.expression:
            values.append(random.randint(0,1))
        self.population.append()
        print(self.population)
        