class Cell:
    alive = False
    next_state = False
    location = [0, 0]
    neighbors = []

    def __init__(self, alive=False, location = [0, 0], neighbors=[]):
        self.alive = alive
        self.next_state = alive
        self.location = location
        self.neighbors = neighbors

    def determine_state(cell):
        alive_count = 0
        for neighbor in cell.neighbors:
            if neighbor.alive == True: alive_count += 1
        
        if cell.alive:
            if alive_count < 2: cell.next_state = False
            elif alive_count >= 4: cell.next_state = False
            else: cell.next_state = True
        else:
            if alive_count == 3: cell.next_state = True
    
    def __str__(self):
        return f"{self.alive}" + str(self.location)