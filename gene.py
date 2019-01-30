import random

class Gene():
    def __init__(self, info):
        self.info = str(info)

    #generates a gene with randomly with numbers between 0 and 1
    def gen_gene(self, size):
        self.info = ""
        for i in range(0, size - 1, 1):
            rando = random.randint(0,1)
            self.info += str(rando)

    def get_info(self):
        return self.info
    
    def print_info(self):
        print(self.info)

  

    