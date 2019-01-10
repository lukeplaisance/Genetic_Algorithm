
#class for holding the symbols, literals, and clauses for the expressions
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")", " "]
        self.clauses = expression.split("*")
        self.values = [0,1,0,0,1,1]
        self.variables = []
        self.literals = []

        for character in expression:
            if character not in self.symbols:
                self.variables.append(character)
                self.variables = list(set(self.variables))
                self.variables.sort()
        print (self.variables)

        mappedLiteral = list(zip(self.variables, self.values))

        print (mappedLiteral)

    


        


    #presto = [a,b,c,1,0,1]
#class for reading from a file
class Parser(object):
    def __init__(self, filename):
        self.file = filename        
        self.open_file = open(self.file, "r")
        self.lines = self.open_file.readlines()

p = Parser("algorithm.txt")
for line in p.lines:
    e = Expression(line)