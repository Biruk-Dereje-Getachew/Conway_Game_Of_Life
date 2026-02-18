class Cell:
    lit = False
    neighbors = []
    def __init__(self, lit=False, neighbors=[]):
        self.lit = lit
        self.neighbors = neighbors
        