class Cell:
    def __init__(self, type, connections):
        self.type = type
        self.connections = connections

    def insertConnection(self, connection):
        self.connections.append(connection)
    
    def details(self):
        print(self.type, self.connections)