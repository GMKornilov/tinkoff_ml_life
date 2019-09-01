import random
from cell import Cell
from copy import deepcopy
from colorama import init, Fore, Back, Style

class ProbabilitiesError(Exception):
    def __init__(self, message):
        super().__init__(message)

class LifeField():

    def __init__(self, size, seed, probas):
        if abs(sum(probas) - 1) >= 1e-8:
            raise ProbabilitiesError("Sum of probabilities should be equal to 1")

        init()
        
        random.seed(seed)
        self.seed = seed

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
        #prints from colored are commented becauuse they didnt work in windows cmd
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == Cell.EMPTY:
                    print(Fore.WHITE + Back.BLACK + "E", end="")
                    #ColoredPrint("E", TextColor.WHITE, end=" ")
                elif self.field[i][j] == Cell.FISH:
                    print(Fore.BLUE + Back.BLACK + "F", end="")
                    #ColoredPrint("F", TextColor.BLUE, end=" ")
                elif self.field[i][j] == Cell.SHRIMP:
                    print(Fore.CYAN + Back.BLACK + "S", end="")
                    #ColoredPrint("S", TextColor.PURPLE, end=" ")
                else:
                    print(Fore.BLACK + Back.WHITE + "R", end="")
                    #ColoredPrint("R", TextColor.BLACK, BackgroundColor.WHITE, end=" ")
                print(Style.RESET_ALL + " ", end="")
            print()
            # ColoredPrint("", TextColor.WHITE, BackgroundColor=BackgroundColor.BLACK)      

    def GetNeighBours(self, i, j, mob):
        '''
        Calculate amount of neighbours of cell with coordinates (i, j) which are equal to mob
        '''
        neighbours = []
        for i_plus, j_plus in [
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1]
        ]:
            if self.InBounds(i + i_plus, j + j_plus) and self.field[i + i_plus][j + j_plus] == mob:
                neighbours.append([i + i_plus, j + j_plus])
        return len(neighbours)

    def InBounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def Proccess(self):
        '''
        Calculate new state of field
        '''
        new_field = deepcopy(self.field)
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == Cell.FISH or self.field[i][j] == Cell.SHRIMP:
                    neighbours = self.GetNeighBours(i, j, self.field[i][j])
                    if neighbours >= 4 or neighbours < 2:
                        new_field[i][j] = Cell.EMPTY
                    else:
                        new_field[i][j] = self.field[i][j]
                elif self.field[i][j] == Cell.EMPTY:
                    fish_neighbours = self.GetNeighBours(i, j, Cell.FISH)
                    shrimp_neighbours = self.GetNeighBours(i, j, Cell.SHRIMP)
                    if fish_neighbours == 3:
                        new_field[i][j] = Cell.FISH
                    elif shrimp_neighbours == 3:
                        new_field[i][j] = Cell.SHRIMP
        self.field = new_field
