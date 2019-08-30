import random
from cell import Cell
from colored import *

class LifeField():

    def __init__(self, size, seed, probas):
        random.seed(seed)

        self.size = size
        self.field = [[None for j in range(self.size)] for i in range(self.size)]
        
        self.probas = probas

        self.GenerateField()

    def GenerateField(self): 
        cellTypes = random.choices(list(Cell), weights=self.probas, k=self.size**2)
        for i in range(self.size):
            for j in range(self.size):
                self.field[i][j] = cellTypes[i * self.size + j]

    def Visualize(self):
        raise NotImplementedError        