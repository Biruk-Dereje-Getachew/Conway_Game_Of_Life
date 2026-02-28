class Cell:
    alive = 0
    next_state = 0
    location = [0, 0]
    neighbors = []

    def __init__(self, alive=0, location = [0, 0]):
        self.alive = alive
        self.next_state = alive # Variable set up to enable evolution of the game
        self.location = location # Location in the grid it will be set in
        self.neighbors = list()

    def determine_state(self): # Logic of the game of life for an individual cell
        alive_count = 0
        for neighbor in self.neighbors:
            if neighbor.alive == 1: alive_count += 1
        
        if self.alive:
            if alive_count < 2: self.next_state = 0
            elif alive_count >= 4: self.next_state = 0
            else: self.next_state = 1
        else:
            if alive_count == 3: self.next_state = 1
    
    def __str__(self):
        return f"{self.alive}" + str(self.location)