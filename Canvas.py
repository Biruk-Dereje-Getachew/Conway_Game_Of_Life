from Cell import Cell
from random import randint
from math import radians, sin, cos

class Canvas:
    size = [0, 0]
    grid = []
    def __init__(self, size=[10, 10], random=False):
        self.size = size
        self.hydrate(random)
        self.neighborate()

    def hydrate(self, random):
        for x in range(self.size[0]):
            row = []
            for y in range(self.size[1]):
                cell_alive = randint(0, 1) if random else 0
                cell = Cell(cell_alive, [x, y])
                row.append(cell)
            self.grid.append(row)
    
    def neighborate(self):
        for row in self.grid:
            for cell in row:

                location = cell.location
                for angle in range(180, -180, -45):
                    rad_angle = radians(angle)
                    cos_angle = round(cos(rad_angle), 2)
                    sin_angle = round(sin(rad_angle), 2)
                    offset_x = int(cos_angle / abs(cos_angle)) if cos_angle != 0 else 0
                    offset_y = int(sin_angle / abs(sin_angle)) if sin_angle != 0 else 0

                    nei_x = location[0] + offset_x
                    nei_y = location[1] + offset_y

                    if (nei_x < 0 or nei_x >= self.size[0] or nei_y < 0 or nei_y >= self.size[1]):
                        continue

                    neighbor = self.grid[nei_x][nei_y]
                    cell.neighbors.append(neighbor)

    def iterate(self):
        for row in self.grid:
            for cell in row:
                cell.determine_state()

        for row in self.grid:
            for cell in row:
                cell.alive = cell.next_state

    def __str__(self):
        canvas_description = ""
        for row in self.grid:
            for cell in row:
                canvas_description += f"{cell.alive} "
            canvas_description += "\n"
        return canvas_description