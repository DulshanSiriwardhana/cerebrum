
class Cell:
    cell_id = 0

    def __init__(self, type, connections):
        Cell.cell_id += 1
        self.cell_id = Cell.cell_id
        self.type = type
        self.connections = connections

    def insertConnection(self, connection):
        self.connections.append(connection)
    
    def details(self):
        return {
            "id": self.cell_id,
            "type": self.type.getType(),
            "connections": self.connections
        }