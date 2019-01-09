
#class for holding the symbols, literals, and clauses for the expressions
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")", " "]
        
        "(!a + c) * (!a + c + !e) * (!b + c + d + !e) * (a + !b + c) * (!e + f)"
        self.clauses = expression.split("*")

        self.literals = []
        for character in expression:
            if character not in self.symbols:
                self.literals.append(character)

        print (self.literals)

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
        
        


