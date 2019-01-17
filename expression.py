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

        #replacing the symbols with operators, then evaluates the expression
        for character in ex:
            ex = ex.replace(self.symbols[0], "not ")
            ex = ex.replace(self.symbols[1], "or")
            ex = ex.replace(self.symbols[2], "and")
        print(eval(ex))
        print(ex)

