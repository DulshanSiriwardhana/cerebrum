import time
import activations

class Cell:
    cell_id = 0

    def __init__(self, type, connections, weight):
        Cell.cell_id += 1
        self.weight = weight or 0
        self.cell_id = Cell.cell_id
        self.type = type
        self.connections = connections

    def insertConnection(self, connection):
        self.connections.append(connection)

    def activate(self, input):
        if self.activate == "normal":
            return activations.normal(input)
        elif self.activate == "sin":
            return activations.sin(input)
        elif self.activate == "cos":
            return activations.cos(input)
        elif self.activate == "exp":
            return activations.exp(input)
        elif self.activate == "piStep":
            return activations.piStep(input)
        else:
            return activations.normal(input)

    def chemistry(self, input):
        myelination = self.type.myelination

        if myelination=="Myelinated":
            return self.activate(input * self.weight)
        else:
            time.sleep(0.01)
            return self.activate(input * self.weight)

    def fire(self, input):
        print("I am thinking bruh: ", input, {
            "id": self.cell_id,
            "type": self.type.getType(),
            "connections": self.connections 
        })
        for contact in self.connections:
            contact.fire(self.chemistry(input))

    def details(self):
        return {
            "id": self.cell_id,
            "type": self.type.getType(),
            "connections": self.connections
        }