import random

#class for holding the symbols, literals, and clauses for the expressions
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")", " "]
        self.clauses = expression.split("*")
        self.values = []
        self.variables = []
        self.expression = expression
        self.new_expression = []
        self.mappedVariable = []

    def get_variables(self):
        #putting each unique character in a list
        for character in self.expression:            
            if character not in self.symbols:
                self.variables.append(character)
                self.variables = list(set(self.variables))
                self.variables.sort()            
        print (self.variables)

    def gen_values(self, expression):
        for i in self.variables:
            self.values.append(random.randint(0,1))
        return self.values

    def map_variables(self):
        #mapping each unique character with a value
        self.mappedVariable = list(zip(self.variables, self.values))
        print (self.mappedVariable)

        #taking the characters in the expression and replacing them with their value
        self.new_expression = self.expression
        for lit in self.mappedVariable:
            self.new_expression = self.new_expression.replace(lit[0], str(lit[1]))

    def replace_symbols(self):
        #replacing the symbols with operators, then evaluates the expression
        for character in self.expression:
            self.new_expression = self.new_expression.replace(self.symbols[0], "not ")
            self.new_expression = self.new_expression.replace(self.symbols[1], "or")
            self.new_expression = self.new_expression.replace(self.symbols[2], "and")
        print(self.new_expression)

    def print_results(self):
        test = bool(eval(self.new_expression))
        print("result : " + str(test))

def main():
    e = Expression("(a) * (b) * (c) * (!d)")
    e.get_variables()
    e.gen_values(e)
    e.map_variables()
    e.replace_symbols()
    e.print_results()

main()
