from Cell import Cell
from random import randint

class Canvas:
    size = [0, 0]
    grid = []
    def __init__(self, size=[10, 10], random=False):
        self.size = size
        self.hydrate(random)

    def hydrate(self, random):
        for x in self.size[0]:
            row = []
            for y in self.size[1]:
                alive = 0 if not random else randint(0, 1)
                location = [x, y]
                cell = Cell(alive, location)
                row.append(cell)
            self.grid.append(row)
        
