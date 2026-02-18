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
        alive = 0 if not random else randint(0, 1)
        cells_to_neighborate = [Cell(alive, [0, 0])] # Initial cell added

        for cell in cells_to_neighborate:
            location = cell.location
            for angle in range(-180, 181, 45):
                angle = radians(angle)
                nei_alive = 0 if not random else randint(0, 1)
                nei_x = location[0] + cos(angle)
                nei_y = location[1] + sin(angle)
                if nei_x < 0 or nei_x >= self.size[0] or nei_y < 0 or nei_y >= self.size[1]:
                    continue
                nei_location = [nei_x, nei_y]
                neighbor = Cell(nei_alive, nei_location)
                cells_to_neighborate.append(neighbor)

                if len(self.grid) < nei_x: self.grid.insert(nei_x, [])
                self.grid[nei_x].insert(nei_y, neighbor)
        
