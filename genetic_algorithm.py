from expression import Expression
from parser import Parser
from gene import Gene
import random

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
        for j in range(0, self.expression):
            values.append(random.randint(0,1))
        self.population.append()
        