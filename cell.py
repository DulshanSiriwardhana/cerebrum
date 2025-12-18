# create cell class that act like a neuron in brain

class Cell:
    def __init__(self, cell_type, threshold):
        self.cell_type = cell_type  # e.g., 'sensory', 'motor', 'interneuron'
        self.threshold = threshold  # activation threshold
        self.potential = 0          # current potential
        self.connections = []       # connected cells

    def connect(self, other_cell):
        """Connect this cell to another cell."""
        self.connections.append(other_cell)

    def receive_signal(self, signal_strength):
        """Receive a signal and update potential."""
        self.potential += signal_strength
        if self.potential >= self.threshold:
            self.fire()

    def fire(self):
        """Fire the cell and send signals to connected cells."""
        print(f"{self.cell_type} cell fired!")
        for cell in self.connections:
            cell.receive_signal(1)  # send a signal of strength 1
        self.potential = 0  # reset potential after firing

