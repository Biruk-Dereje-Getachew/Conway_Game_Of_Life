class Cell:
    alive = 0
    next_state = 0
    location = [0, 0]
    neighbors = []

    def __init__(self, alive=0, location = [0, 0], neighbors=[]):
        self.alive = alive
        self.next_state = alive
        self.location = location
        self.neighbors = neighbors

    def determine_state(cell):
        alive_count = 0
        for neighbor in cell.neighbors:
            if neighbor.alive == 1: alive_count += 1
        
        if cell.alive:
            if alive_count < 2: cell.next_state = 0
            elif alive_count >= 4: cell.next_state = 0
            else: cell.next_state = 1
        else:
            if alive_count == 3: cell.next_state = 1
    
    def __str__(self):
        return f"{self.alive}" + str(self.location)