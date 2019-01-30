from expression import Expression
from gene import Gene
import random
from operators import *

#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.read_file = open(self.file, "r")
        self.lines = self.read_file.readlines()


class Genetic_Algorithm(object):
    def __init__(self, expression):
        self.population = []
        self.parser = Parser("exp.txt")
        self.generation = 1
        self.is_finished = False
        self.values = []
        self.info_file = open("info_file.txt", "w+")
        self._expression = expression

    def show_info(self):
        self.info_file.write('\n')
        self.info_file.write('Finished?:' + str(self.is_finished) + '\n')

    #generates the population
    def gen_population(self, size):
        population = []
        for i in range(0, size - 1, 1):
            g = Gene("")
            g.gen_gene(size)
            population.append(g)
        return population

    def determine_fitness(self):
        tmp = self._expression.new_expression.split("and")
        print(tmp)
        return self._expression.print_results()
            
    def run_algorithm(self):
        self._expression.get_variables()
        self._expression.gen_values()
        self._expression.map_variables()
        self._expression.replace_symbols()
        gene_count = len(self._expression.variables)
        self.population = self.gen_population(gene_count)

        while not self.is_finished:
            print ('Generation: ' + str(self.generation))
            if(self.generation >= 500):
                self.show_info()
                self.determine_fitness()
                return
           
            self.is_finished = self.determine_fitness()
            self.show_info()

            if(self.is_finished):
                print("Solution: " + self.population[0].get_info())
                self.show_info()
                return

            current_generation = select_parent(self.population)
            self.population = []  
            self.population = cross_over(current_generation[0], current_generation[1], int((gene_count / 2)))
            self.generation += 1
            for gene in self.population:
                gene.info = mutate(gene)

        self.info_file.close()

            

def main():
    expressions = []
    p = Parser("exp.txt")
    for line in p.lines:
        expressions.append(Expression(line))
    for exp in expressions:
        a = Genetic_Algorithm(exp)
        a.run_algorithm()
        a.info_file.close()
    print ("finished")
main()


        
    