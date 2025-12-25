
class Cell:
    cell_id = 0
    def __init__(self, type, connections):
        self.cell_id=self.cell_id+1
        self.type = type
        self.connections = connections

    def insertConnection(self, connection):
        self.connections.append(connection)
    
    def details(self):
        return self