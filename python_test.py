
#class for holding the symbols, literals, and clauses for the expressions
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")", " "]
        self.clauses = expression.split("*")
        self.population= ['0','1','0','0','1','1']
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
        mappedLiteral = list(zip(self.variables, self.population))
        print (mappedLiteral)

        #taking the characters in the expression and replacing them with their value
        ex = expression
        for lit in mappedLiteral:
            ex = ex.replace(lit[0], lit[1])
        print(ex) 

    def cross_over(self, other, pivot):
        other = ['1','1','0','0','1','1']
        newGene = []
        i = 0
        for item in self.population:
            newGene.append(item)
            i += 1
            if i == pivot:
                break
        for x in range(pivot, other.__len__()):
            newGene.append(other.index[x])
        print(newGene)


expr = Expression("(!a + c) * (!a + c + !e) * (!b + c + d + !e) * (a + !b + c) * (!e + f)")




#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.open_file = open(self.file, "r")
        self.lines = self.open_file.readlines()

p = Parser("algorithm.txt")
for line in p.lines:
    e = Expression(line)    


