class Cell:
    alive = False
    location = [0, 0]
    neighbors = []
    def __init__(self, alive=False, location = [0, 0], neighbors=[]):
        self.alive = alive
        self.location = location
        self.neighbors = neighbors

    def determine_state(cell):
        alive = 0
        for neighbor in cell.neighbors:
            if neighbor.alive == True: alive += 1
        
        if cell.alive:
            if alive < 2: cell.alive = False
            elif alive >= 4: cell.alive = False
        else:
            if alive == 3: cell.alive = True
    
    def __str__(self):
        return str(self.location)