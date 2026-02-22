from Grid import Grid
from Helpers import square
from time import sleep
import turtle

class Canvas:
    _grid = None
    _turtle = None
    _width = 5
    _initial = 1


    def __init__(self, size=[10, 10], random=False, width=20):
        self._grid = Grid(size, random)
        self._width = width
        self._turtle = turtle.Turtle()
        self._turtle.screen.tracer(0)

    def draw(self):
        self._grid.iterate()
        for row in self._grid.grid:
            for cell in row:
                if cell.next_state == cell.alive and not self._initial: continue

                color = "aquamarine" if cell.next_state else "white"
                square(self._turtle, color, self._width, cell.location)
        self._initial = 0
        self._turtle.screen.update()

    def simulate(self, delay):
        while True:
            self.draw()
            sleep(delay)