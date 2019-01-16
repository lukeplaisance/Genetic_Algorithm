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

        #replacing the symbols with operators
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


#function that crosses over parts of the previous populations to make a new one
def cross_over(geneOne, geneTwo):
    pivot = int(random.randint(1, 3))
    return (geneOne[:pivot] + geneTwo[pivot:], geneTwo[:pivot] + geneOne[pivot:])


a = [0,1,1,0,1,0]
b = [1,1,0,0,0,1]
cross = cross_over(a, b)
print(cross)

