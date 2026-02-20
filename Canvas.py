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
        initial_cell = Cell(alive, [0, 0])
        cells_to_neighborate = [initial_cell] # Initial cell added
        self.grid.append([initial_cell])
        track_neighbors = {(initial_cell.location[0], initial_cell.location[1])}

        for cell in cells_to_neighborate:
            location = cell.location

            for angle in range(180, -180, -45):
                rad_angle = radians(angle)
                cos_angle = round(cos(rad_angle))
                sin_angle = round(sin(rad_angle))
                offset_x = int(cos_angle / abs(cos_angle)) if cos_angle != 0 else 0
                offset_y = int(sin_angle / abs(sin_angle)) if sin_angle != 0 else 0

                nei_x = location[0] + offset_x
                nei_y = location[1] + offset_y

                if (nei_x < 0 or nei_x >= self.size[1] or nei_y < 0 or nei_y >= self.size[0]) or ((nei_x, nei_y) in track_neighbors):
                    continue

                nei_location = [nei_x, nei_y]
                nei_alive = 0 if not random else randint(0, 1)

                neighbor = Cell(nei_alive, nei_location)
                cells_to_neighborate.append(neighbor)
                track_neighbors.add((nei_x, nei_y))

                if len(self.grid) <= nei_x: self.grid.insert(nei_x, [])
                if nei_y >= len(self.grid[nei_x]):
                    for _ in range((nei_y + 1) - len(self.grid[nei_x])):
                        self.grid[nei_x].append(object())
                self.grid[nei_x][nei_y] = neighbor

    def __str__(self):
        canvas_description = ""
        for row in self.grid:
            for cell in row:
                canvas_description += f"{cell.alive} "
            canvas_description += "\n"
        return canvas_description