from Cell import Cell
from random import randint
from math import radians, sin, cos

class Canvas:
    size = [0, 0]
    grid = []
    def __init__(self, size=[10, 10], random=False):
        self.size = size
        self.hydrate(random)

    def hydrate(self, random):
        for x in range(self.size[0]):
            row = []
            for y in range(self.size[1]):
                cell_alive = randint(0, 1) if random else 0
                cell = Cell(cell_alive, [x, y])
                row.append(cell)
            self.grid.append(row)

    def __str__(self):
        canvas_description = ""
        for row in self.grid:
            for cell in row:
                canvas_description += f"{cell.alive} "
            canvas_description += "\n"
        return canvas_description