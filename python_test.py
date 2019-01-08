
class Expression(object):
    def __init__(self, expression):
        self.symbols = ["!", "+", "*", "(", ")"]
        self.literals = []
        self.variables = {}
        self.clauses = expression.split("*")

    

class Parcer(Expression):
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.read_line = file.readline()
        for self.read_line in file:
            variables = clauses






file = open("algorithm.txt", "r")
print(file.read())
file.close