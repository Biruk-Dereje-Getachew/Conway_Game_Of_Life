class Cell:
    alive = False
    location = [0, 0]
    neighbors = []
    def __init__(self, alive=False, location = [0, 0], neighbors=[]):
        self.alive = alive
        self.location = location
        self.neighbors = neighbors