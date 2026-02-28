from Cell import Cell
from random import randint
from math import radians, sin, cos

class Grid:
    _size = [0, 0]
    grid = []
    def __init__(self, size=[10, 10], random=False):
        self._size = size
        self.hydrate(random)
        self.neighborate()

    def hydrate(self, random): # Function that fills the grid with Cells according to the size given in the constructor
        for x in range(self._size[0]):
            row = []
            for y in range(self._size[1]):
                cell_alive = randint(0, 1) if random else 0
                cell = Cell(cell_alive, [x, y])
                row.append(cell)
            self.grid.append(row)
    
    def neighborate(self): # Function to give each Cell in the grid its neighbors
        for row in self.grid:
            for cell in row:

                location = cell.location
                ''' The neighbors of a cell are located in one of eight positions
                        Center left
                        Top left
                        Top center
                        Top right
                        Center right
                        Bottom right
                        Bottom center
                        Bottom left
                    The movement of a clock starting from 9:00 captures this perfectly. If we go in 45 degree increments the cos and the sin value of the angle, as measured from the positive x axis, will give us what we need to add (or subtract if it is a negative value) from the location of the cell for whom we are looking for neighbors to get the location of the neighboring cells.
                    Look at the following example
                        Location of a cell: [4, 5]
                        Location of the neighbor to the left of the cell: [3, 5]
                        Corresponding angle measured from the positive x axis to the location of the neighbor with the cell being origin: 180
                        cos(180) = -1
                        sin(180) = 0
                        Location of cell + [cos value, sin value] = Location of neighbor
                        '''
                for angle in range(180, -180, -45):
                    rad_angle = radians(angle)
                    cos_angle = round(cos(rad_angle), 2)
                    sin_angle = round(sin(rad_angle), 2)
                    offset_x = int(cos_angle / abs(cos_angle)) if cos_angle != 0 else 0
                    offset_y = int(sin_angle / abs(sin_angle)) if sin_angle != 0 else 0

                    nei_x = location[0] + offset_x
                    nei_y = location[1] + offset_y

                    # If the location of a potential neighbor is out of bounds of the grid, it is discarded
                    if (nei_x < 0 or nei_x >= self._size[0] or nei_y < 0 or nei_y >= self._size[1]):
                        continue

                    neighbor = self.grid[nei_x][nei_y]
                    cell.neighbors.append(neighbor)

    def iterate(self): # Function that moves to the next round of the game
        for row in self.grid:
            for cell in row:
                cell.alive = cell.next_state
        for row in self.grid:
            for cell in row:
                cell.determine_state()


    def __str__(self):
        canvas_description = ""
        for row in self.grid:
            for cell in row:
                canvas_description += f"{cell.alive} "
            canvas_description += "\n"
        return canvas_description