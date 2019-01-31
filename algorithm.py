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
        self.scored_population = []
        self.parser = Parser("exp.txt")
        self.generation = 1
        self.is_finished = False
        self.values = []
        self.info_file = open("info_file.txt", "a+")
        self._expression = expression

    def show_info(self):
        self.info_file.write('\n')
        self.info_file.write('Finished?: ' + str(self.is_finished) + '\n')
        for gene in self.scored_population:
            info = (gene[0].get_info(), str(gene[1]), 'Generation: ' + str(self.generation))
            self.info_file.write(str(info) + '\n')

    #generates the population
    def gen_population(self, size):
        population = []
        for i in range(0, size - 1, 1):
            g = Gene("")
            g.gen_gene(size)
            population.append(g)
        return population

    def determine_fitness(self):
        for gene in self.population:
            gene_length = len(gene.get_info())
            clauses = self._expression.new_expression.split("and")
            gene.fitness = s_determine_fitness(clauses)

        self.scored_population.append(gene.fitness)
        self.population = []
        for score in self.scored_population:
            self.population.append(score)

                    
    def determine_solution(self):
        tmp = self._expression.new_expression.split("and")
        print(tmp)
            
        return self._expression.test_results()
            
    def run_algorithm(self):
        #gets an expression with mapped values and symbols
        self._expression.get_variables()
        self._expression.gen_values()
        self._expression.map_variables()
        self._expression.replace_symbols()

        #generates the population 
        gene_count = len(self._expression.variables)
        self.population = self.gen_population(gene_count)

        #while the algorithm is not finished make another generation until you reach 100
        while not self.is_finished:
            print ('Generation: ' + str(self.generation))
            if(self.generation >= 500):
                self.show_info()
                return
           
           #determine the fitness score of the clauses and checks the solution to see if the algo is finished
            self.determine_fitness()
            self.is_finished = self.determine_solution()
            self.show_info()

            #if it is finished, print out the solution
            if(self.is_finished):
                print("Solution: " + self.population[0].get_info())
                self.show_info()
                return

            #selects parents for the next generation
            current_generation = select_parent(self.population)
            self.population = []

            #call cross_over and the mutate methods on the current generation
            self.population = cross_over(current_generation[0], current_generation[1], int((gene_count / 2)))
            self.generation += 1
            for gene in self.population:
                gene.info = mutate(gene)

        #close the info file
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


        
    